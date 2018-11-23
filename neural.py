import random


class NeuralNetwork(object):
    def __init__(self, inputs):
        self.hidden_layer = Layer(4, inputs)
        self.output = Layer(4, self.hidden_layer.neurons)


class Layer(object):

    def __init__(self, n_neurons: int, previous_layer):
        self.n_neuron_per_layer = n_neurons
        self.neurons = []
        for i in range(n_neurons):
            self.neurons.append(Neuron(previous_layer))


class Neuron(object):
    def __init__(self, inputs: []):
        self.previous_layer = inputs
        self.weights = []
        for i in range(len(inputs)):
            self.weights.append(random.uniform(0, 1))

    def get_output(self):
        result = 0
        for i in range(len(self.weights)):
            result += self.weights[i] * self.previous_layer[i].get_output()
