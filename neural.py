class NeuralNetwork(object):
    def __init__(self, n_inputs=4, n_hidden_layers=1, n_neuron_per_layer=3, n_outputs=4):
        self.n_inputs = n_inputs
        self.n_hidden_layers = n_hidden_layers
        self.hidden_layers = []
        for i in range(n_hidden_layers):
            self.hidden_layers.append(Layer(n_neuron_per_layer))
        self.n_outputs = n_outputs


class Layer(object):

    def __init__(self, n_neuron_per_layer):
        self.n_neuron_per_layer = n_neuron_per_layer
        self.neurons = []
        for i in range(n_neuron_per_layer):
            self.neurons.append(Neuron())


class Neuron(object):
    def __init__(self, n_inputs, weights):
        self.n_inputs = n_inputs
        self.weights = weights
