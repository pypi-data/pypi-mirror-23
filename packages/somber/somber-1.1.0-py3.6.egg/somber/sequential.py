import logging
import json
import cupy as cp
import numpy as np

from .som import Som
from .utils import expo, linear, np_min, np_max, resize

logger = logging.getLogger(__name__)


class Sequential(Som):
    """
    A base class for sequential SOMs, removing some code duplication.

    Not usable stand-alone.
    """

    def __init__(self,
                 map_dim,
                 data_dim,
                 learning_rate,
                 sigma,
                 lrfunc=expo,
                 nbfunc=expo,
                 min_max=np_min):
        """
        A base class for sequential SOMs, removing some code duplication.

        :param map_dim: A tuple describing the MAP size.
        :param data_dim: The dimensionality of the input matrix.
        :param learning_rate: The learning rate.
        :param sigma: The neighborhood factor.
        :param lrfunc: The function used to decrease the learning rate.
        :param nbfunc: The function used to decrease the neighborhood
        :param min_max: The function used to determine the winner.
        """
        super().__init__(map_dim,
                         data_dim,
                         learning_rate,
                         sigma,
                         lrfunc,
                         nbfunc,
                         min_max)

    def _ensure_params(self, X):
        """
        Ensure the parameters are of the correct type.

        :param X: The input data
        :return: None
        """
        xp = cp.get_array_module(X)
        self.weights = xp.asarray(self.weights, xp.float32)
        self.context_weights = xp.asarray(self.context_weights, xp.float32)

    def _init_prev(self, X):
        """
        Safely initializes the first previous activation.

        :param X: The input data.
        :return: A matrix of the appropriate size for simulating contexts.
        """
        xp = cp.get_array_module(X)
        return xp.zeros((X.shape[1], self.weight_dim))

    def _create_batches(self, X, batch_size):
        """
        Create subsequences out of a sequential piece of data.

        Assumes ndim(X) == 2.

        This function will append zeros to the end of your data to make
        sure all batches even-sized.

        :param X: A numpy array, representing your input data.
        Must have 2 dimensions.
        :param batch_size: The desired batch size.
        :return: A batched version of your data
        """
        xp = cp.get_array_module(X)

        self.progressbar_interval = 1
        self.progressbar_mult = batch_size

        if batch_size > X.shape[0]:
            batch_size = X.shape[0]

        max_x = int(xp.ceil(X.shape[0] / batch_size))
        # This line first resizes the data to
        X = resize(X, (batch_size, max_x, X.shape[1]))
        # Transposes it to (len(X) / batch_size, batch_size, data_dim)
        return X.transpose((1, 0, 2))

    def forward(self, x, **kwargs):
        """
        Empty.

        :param x: the input data
        :return None
        """
        pass

    def _predict_base(self, X, batch_size=100):
        """
        Predict distances to some input data.

        :param X: The input data.
        :return: An array of arrays, representing the activation
        each node has to each input.
        """
        self._check_input(X)

        xp = cp.get_array_module(X)
        batched = self._create_batches(X, batch_size)

        activations = []

        activation = self._init_prev(batched)

        for x in batched:
            activation = self.forward(x, prev_activation=activation)[0]
            activations.append(activation)

        act = xp.asarray(activations, dtype=xp.float32).transpose((1, 0, 2))
        act = act[:X.shape[0]]
        return act.reshape(X.shape[0], self.weight_dim)

    def generate(self, num_to_generate, starting_place):
        """
        Generate data based on some initial position.

        :param num_to_generate: The number of tokens to generate
        :param starting_place: The place to start from. This should
        be a vector equal to a context weight.
        :return:
        """
        res = []
        activ = starting_place
        for x in range(num_to_generate):
            m = np.argmax(activ, 0)
            res.append(m)
            activ = self.context_weights[m]

        return res[::-1]


class Recursive(Sequential):

    def __init__(self,
                 map_dim,
                 data_dim,
                 learning_rate,
                 alpha,
                 beta,
                 sigma=None,
                 lrfunc=expo,
                 nbfunc=expo):
        """
        A recursive SOM.

        A recursive SOM models sequences through context dependence by not only
        storing the exemplars in weights, but also storing which exemplars
        preceded them. Because of this organization, the SOM can recursively
        "remember" short sequences, which makes it attractive for simple
        sequence problems, e.g. characters or words.

        :param map_dim: A tuple of map dimensions,
        e.g. (10, 10) instantiates a 10 by 10 map.
        :param data_dim: The data dimensionality.
        :param learning_rate: The learning rate, which is decreased
        according to some function.
        :param lrfunc: The function to use in decreasing the learning rate.
        The functions are defined in utils. Default is exponential.
        :param nbfunc: The function to use in decreasing the neighborhood size.
        The functions are defined in utils. Default is exponential.
        :param alpha: a float value, specifying how much weight the
        input value receives in the BMU calculation.
        :param beta: a float value, specifying how much weight the context
        receives in the BMU calculation.
        :param sigma: The starting value for the neighborhood size, which is
        decreased over time. If sigma is None (default), sigma is calculated as
        ((max(map_dim) / 2) + 0.01), which is generally a good value.
        """

        super().__init__(map_dim,
                         data_dim,
                         learning_rate,
                         lrfunc,
                         nbfunc,
                         sigma,
                         min_max=np_max)

        self.context_weights = np.zeros((self.weight_dim, self.weight_dim),
                                        dtype=np.float32)
        self.alpha = alpha
        self.beta = beta

    def _propagate(self, x, influences, **kwargs):
        """
        Propagate a single batch of examples through the network.

        First computes the activation the maps neurons, given a batch.
        Then updates the weights of the neurons by taking the mean of
        differences over the batch.

        :param X: an array of data
        :param influences: The influence at the current epoch,
        given the learning rate and map size
        :return: A vector describing activation values for each unit.
        """
        prev = kwargs['prev_activation']

        activation, diff_x, diff_y = self.forward(x, prev_activation=prev)
        self.backward(diff_x, influences, activation, difference_y=diff_y)
        return activation

    def forward(self, x, **kwargs):
        """
        Get the best matching units, based on euclidean distance.

        The euclidean distance between the context vector and context weights
        and input vector and weights are used to estimate the BMU. The
        activation of the units is the sum of the distances, weighed by two
        constants, alpha and beta.

        The exponent of the negative of this value describes the activation
        of the units. This function is bounded between 0 and 1, where 1 means
        the unit matches well and 0 means the unit doesn't match at all.

        :param x: A batch of data.
        :return: The activation, the difference between the input and weights.
        and the difference between the context and weights.
        """
        prev = kwargs['prev_activation']
        # Differences is the components of the weights subtracted from
        # the weight vector.
        distance_x, diff_x = self.distance_function(x, self.weights)
        distance_y, diff_y = self.distance_function(prev, self.context_weights)

        x_ = distance_x * self.alpha
        y_ = distance_y * self.beta
        activation = cp.exp(-(x_ + y_))

        return activation, diff_x, diff_y

    def backward(self, diff_x, influences, activation, **kwargs):
        """
        Backward pass through the network, including update.

        :param diff_x: The difference between the input data and the weights
        :param influences: The influences at the current time-step
        :param activation: The activation at the output
        :param kwargs:
        :return: None
        """
        xp = cp.get_array_module(diff_x)

        diff_y = kwargs['difference_y']
        influence = self._apply_influences(activation, influences)
        # Update
        x_update = self._calculate_update(diff_x, influence)
        self.weights += x_update.mean(0)
        y_update = self._calculate_update(diff_y, influence)
        self.context_weights += xp.squeeze(y_update.mean(0))

    @classmethod
    def load(cls, path, array_type=np):
        """
        Load a recursive SOM from a JSON file.

        You can use this function to load weights of other SOMs.
        If there are no context weights, the context weights will be set to 0.

        :param path: The path to the JSON file.
        :param array_type: The type of array to load
        :return: A RecSOM.
        """
        data = json.load(open(path))

        weights = data['weights']
        weights = array_type.asarray(weights, dtype=cp.float32)
        datadim = weights.shape[1]

        dimensions = data['dimensions']
        lrfunc = expo if data['lrfunc'] == 'expo' else linear
        nbfunc = expo if data['nbfunc'] == 'expo' else linear
        lr = data['lr']
        sigma = data['sigma']

        try:
            context_weights = data['context_weights']
            context_weights = array_type.asarray(context_weights,
                                                 dtype=cp.float32)
        except KeyError:
            context_weights = array_type.zeros((len(weights), len(weights)))

        try:
            alpha = data['alpha']
            beta = data['beta']
        except KeyError:
            alpha = 3.0
            beta = 1.0

        s = cls(dimensions,
                datadim,
                lr,
                lrfunc=lrfunc,
                nbfunc=nbfunc,
                sigma=sigma,
                alpha=alpha,
                beta=beta)

        s.weights = weights
        s.context_weights = context_weights
        s.trained = True

        return s

    def save(self, path):
        """
        Save a SOM to a JSON file.

        :param path: The path to the JSON file that will be created
        :return: None
        """
        dicto = {}
        dicto['weights'] = [[float(w) for w in x] for x in self.weights]
        dicto['context_weights'] = [[float(w) for w in x] for
                                    x in self.context_weights]
        dicto['dimensions'] = self.map_dimensions
        dicto['lrfunc'] = 'expo' if self.lrfunc == expo else 'linear'
        dicto['nbfunc'] = 'expo' if self.nbfunc == expo else 'linear'
        dicto['lr'] = self.learning_rate
        dicto['sigma'] = self.sigma
        dicto['alpha'] = self.alpha
        dicto['beta'] = self.beta

        json.dump(dicto, open(path, 'w'))

    def quant_error(self, X, batch_size=1):
        """
        Calculate the quantization error.

        Find the the minimum euclidean distance between the units and
        some input.

        :param X: Input data.
        :param batch_size: The batch size to use when calculating
        the quantization error. Recommended to not raise this.
        :return: A vector of numbers, representing the quantization error
        for each data point.
        """
        dist = self._predict_base(X, batch_size)
        res = 1 - self.min_max(dist, 1)[0]
        xp = cp.get_array_module(res)
        if xp == np:
            return res
        else:
            return res.get()


class Merging(Sequential):

    def __init__(self,
                 map_dim,
                 data_dim,
                 learning_rate,
                 alpha,
                 beta,
                 sigma=None,
                 lrfunc=expo,
                 nbfunc=expo,
                 min_max=np_min):
        """
        A merging som.

        :param map_dim: A tuple of map dimensions,
        e.g. (10, 10) instantiates a 10 by 10 map.
        :param data_dim: The data dimensionality.
        :param learning_rate: The learning rate, which is decreased
        according to some function.
        :param lrfunc: The function to use in decreasing the learning rate.
        The functions are defined in utils. Default is exponential.
        :param nbfunc: The function to use in decreasing the neighborhood size.
        The functions are defined in utils. Default is exponential.
        :param alpha: Controls the rate of context dependence, where 0 is low
        context dependence, and 1 is high context dependence. Should start at
        low values (e.g. 0.0 to 0.05)
        :param beta: A float between 1 and 0 specifying the influence of
        context on previous weights. Static, usually 0.5.
        :param sigma: The starting value for the neighborhood size, which is
        decreased over time. If sigma is None (default), sigma is calculated as
        ((max(map_dim) / 2) + 0.01), which is generally a good value.
        """
        super().__init__(map_dim,
                         data_dim,
                         learning_rate,
                         lrfunc,
                         nbfunc,
                         sigma,
                         min_max)

        self.alpha = alpha
        self.beta = beta
        self.context_weights = np.ones_like(self.weights)
        self.entropy = 0

    def _propagate(self, x, influences, **kwargs):
        """
        Process a single batch of examples.

        :param X: a numpy array of data
        :param influences: The influence at the current epoch,
        given the learning rate and map size
        :return: A vector describing activation values for each unit.
        """
        prev = kwargs['prev_activation']

        # Get the indices of the Best Matching Units, given the data.
        activation, diff_x, diff_y = self.forward(x, prev_activation=prev)
        self.backward(diff_x, influences, activation, difference_y=diff_y)

        return activation

    def _entropy(self, prev_bmus, prev_update):
        """
        Calculate the entropy activation pattern.

        Merging SOMS perform better when their weight-based activation profile
        has high entropy, as small changes in context will then be able to have
        a larger effect.

        This is reflected in this function, which increases the importance of
        context by decreasing alpha if the entropy decreases. The function uses
        a very large momentum term of 0.9 to make sure the entropy does not
        rise or fall too sharply.

        :param prev_bmus: The previous BMUs.
        :param prev_update: The previous update, used as a momentum term.
        :return:
        """
        xp = cp.get_array_module(prev_bmus)

        prev_bmus = xp.array(list(prev_bmus.values()), dtype=xp.float32)
        prev_bmus = prev_bmus / xp.sum(prev_bmus)

        new_entropy = -xp.sum(prev_bmus * xp.nan_to_num(cp.log2(prev_bmus)))
        entropy_diff = (new_entropy - self.entropy)

        update = (entropy_diff * 0.1) + (prev_update * 0.9)

        self.entropy = new_entropy

        logger.info("Entropy: {0}".format(new_entropy))

        return update

    def forward(self, x, **kwargs):
        """
        Get the best matching units, based on euclidean distance.

        :param x: The input vector
        :return: An integer, representing the index of the best matching unit.
        """
        prev_bmu = self.min_max(kwargs['prev_activation'], 1)[1]

        # weight part of context.
        context = (1 - self.beta) * self.weights[prev_bmu]
        # previous part of context.
        context += self.beta * self.context_weights[prev_bmu]

        distances_x, diff_x = self.distance_function(x,
                                                     self.weights)

        distances_y, diff_y = self.distance_function(context,
                                                     self.context_weights)

        # BMU is based on a weighted addition of current and
        # previous activation.
        act = (distances_x * 1 - self.alpha) + (distances_y * self.alpha)

        return act, diff_x, diff_y

    def backward(self, diff_x, influences, activation, **kwargs):
        """
        Backward pass through the network, including update.

        :param diff_x: The difference between the input data and the weights
        :param influences: The influences at the current time-step
        :param activation: The activation at the output
        :param kwargs:
        :return: None
        """
        diff_y = kwargs['difference_y']
        influence = self._apply_influences(activation, influences)
        # Calculate updates
        update = self._calculate_update(diff_x, influence)
        context_update = self._calculate_update(diff_y, influence)

        # Assign updates
        self.weights += update.mean(0)
        self.context_weights += context_update.mean(0)

    def _predict_base(self, X, batch_size=1):
        """
        Predict distances to some input data.

        :param X: The input data.
        :return: A matrix, representing the activation
        each node has to each input.
        """
        self._check_input(X)

        xp = cp.get_array_module(X)
        X = self._create_batches(X, batch_size=batch_size)
        distances = []

        prev = self._init_prev(X)

        for x in X:
            prev = self.forward(x, prev_activation=prev)[0]
            distances.extend(prev)

        return xp.array(distances, dtype=xp.float32)

    def generate(self, num_to_generate, starting_place):
        """
        Generate data based on some initial position.

        :param num_to_generate: The number of tokens to generate
        :param starting_place: The place to start from. This should
        be a vector equal to a context weight.
        :return:
        """
        res = []

        # Calculate the first BMU.
        start_idx = np.argmin(self.distance_function(starting_place[None, :],
                              self.weights)[0])

        activ = self.weights[start_idx]
        for x in range(num_to_generate):
            p, _ = self.distance_function(activ[None, :], self.context_weights)
            p = np.argmin(p)
            res.append(p)
            activ = self.weights[p]

        return res

    @classmethod
    def load(cls, path, array_type=np):
        """
        Load a SOM from a JSON file.

        A normal SOM can be loaded via this method. Any attributes not present
        in the loaded JSON will be initialized to sane values.

        :param path: The path to the JSON file.
        :param array_type: The array type to use.
        :return: A trained mergeSom.
        """
        data = json.load(open(path))

        weights = data['weights']
        weights = array_type.array(weights, dtype=array_type.float32)

        datadim = weights.shape[1]
        dimensions = data['dimensions']

        lrfunc = expo if data['lrfunc'] == 'expo' else linear
        nbfunc = expo if data['nbfunc'] == 'expo' else linear
        lr = data['lr']
        sigma = data['sigma']

        try:
            context_weights = data['context_weights']
            context_weights = array_type.array(context_weights,
                                               dtype=array_type.float32)
        except KeyError:
            context_weights = array_type.ones(weights.shape)

        try:
            alpha = data['alpha']
            beta = data['beta']
            entropy = data['entropy']
        except KeyError:
            alpha = 0.0
            beta = 0.5
            entropy = 0.0

        s = cls(dimensions,
                datadim,
                lr,
                lrfunc=lrfunc,
                nbfunc=nbfunc,
                sigma=sigma,
                alpha=alpha,
                beta=beta)

        s.entropy = entropy
        s.weights = weights
        s.context_weights = context_weights
        s.trained = True

        return s

    def save(self, path):
        """
        Save the merging SOM to a JSON file.

        :param path: The path to which to save the JSON file.
        :return: None
        """
        to_save = {}
        to_save['weights'] = [[float(w) for w in x] for x in self.weights]
        to_save['context_weights'] = [[float(w) for w in x]
                                      for x in self.context_weights]
        to_save['dimensions'] = self.map_dimensions
        to_save['lrfunc'] = 'expo' if self.lrfunc == expo else 'linear'
        to_save['nbfunc'] = 'expo' if self.nbfunc == expo else 'linear'
        to_save['lr'] = self.learning_rate
        to_save['sigma'] = self.sigma
        to_save['alpha'] = self.alpha
        to_save['beta'] = self.beta
        to_save['entropy'] = self.entropy

        json.dump(to_save, open(path, 'w'))
