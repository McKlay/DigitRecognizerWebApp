# network/neural_network.py
import numpy as np
from models.layers import Dense, ActivationReLU, ActivationSoftmax
from models.losses import SoftmaxClassifier

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.layer1 = Dense(input_size, hidden_size)
        self.activation1 = ActivationReLU()
        self.layer2 = Dense(hidden_size, output_size)
        self.activation2 = ActivationSoftmax()
        self.loss_function = SoftmaxClassifier()

    def forward(self, inputs):
        output = self.layer1.forward(inputs)
        output = self.activation1.forward(output)
        output = self.layer2.forward(output)
        return output

    def backward(self, output, targets):
        # Backward pass through loss (Softmax combined with Cross-Entropy)
        grad_loss = self.loss_function.backward(output, targets)

        # Backward pass through second Dense layer
        grad = self.layer2.backward(grad_loss)

        # Backward pass through ReLU activation
        grad = self.activation1.backward(grad)

        # Backward pass through first Dense layer
        grad = self.layer1.backward(grad)

    def train(self, x_train, y_train, learning_rate, batch_size):
        num_samples = x_train.shape[0]
        indices = np.arange(num_samples)
        np.random.shuffle(indices)

        x_train = x_train[indices]
        y_train = y_train[indices]

        total_loss = 0
        num_batches = num_samples // batch_size

        for batch_idx in range(num_batches):
            start = batch_idx * batch_size
            end = start + batch_size
            batch_x = x_train[start:end]
            batch_y = y_train[start:end]

            # Forward pass
            outputs = self.forward(batch_x)

            # Compute loss
            loss = self.loss_function.forward(outputs, batch_y)
            total_loss += loss

            # Backward pass
            self.backward(self.loss_function.probabilities, batch_y)

            # Gradient descent step
            self.layer1.weights -= learning_rate * self.layer1.dweights
            self.layer1.biases -= learning_rate * self.layer1.dbiases
            self.layer2.weights -= learning_rate * self.layer2.dweights
            self.layer2.biases -= learning_rate * self.layer2.dbiases

        avg_loss = total_loss / num_batches
        return avg_loss

    def evaluate(self, x_test, y_test):
        outputs = self.forward(x_test)
        predictions = np.argmax(outputs, axis=1)
        labels = np.argmax(y_test, axis=1)
        accuracy = np.mean(predictions == labels) * 100
        return accuracy
