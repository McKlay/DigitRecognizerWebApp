# network/layers.py
import numpy as np

class Dense:
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        # Save input for backward pass
        self.inputs = inputs
        # Linear combination
        self.output = np.dot(inputs, self.weights) + self.biases
        return self.output

    def backward(self, dvalues):
        # Gradients on parameters
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        # Gradient on values for previous layer
        self.dinputs = np.dot(dvalues, self.weights.T)
        return self.dinputs


class ActivationReLU:
    def forward(self, inputs):
        self.inputs = inputs
        # ReLU activation: max(0, x)
        self.output = np.maximum(0, inputs)
        return self.output

    def backward(self, dvalues):
        # Gradient is 0 when input <= 0
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0
        return self.dinputs


class ActivationSoftmax:
    def forward(self, inputs):
        self.inputs = inputs
        # Shift values to avoid numerical instability
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
        return self.output

    def backward(self, dvalues):
        # Will be handled combined with Cross-Entropy loss
        pass  # Not implemented separately for now
