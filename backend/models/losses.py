# network/losses.py
import numpy as np

class SoftmaxClassifier:
    def forward(self, inputs, y_true):
        # Save input values
        self.inputs = inputs

        # Softmax activation
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        self.probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)

        # Loss calculation
        samples = len(inputs)
        correct_confidences = self.probabilities[range(samples), np.argmax(y_true, axis=1)]
        negative_log_likelihoods = -np.log(correct_confidences)
        loss = np.mean(negative_log_likelihoods)
        return loss

    def backward(self, dvalues, y_true):
        # Number of samples
        samples = len(dvalues)

        # If labels are one-hot encoded, convert them back to integers
        if len(y_true.shape) == 2:
            y_true = np.argmax(y_true, axis=1)

        # Copy so we don't modify original
        self.dinputs = dvalues.copy()
        self.dinputs[range(samples), y_true] -= 1
        self.dinputs = self.dinputs / samples
        return self.dinputs
