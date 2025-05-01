# backend/utils/model_loader.py
import numpy as np
from backend.models.neural_network import NeuralNetwork

def load_trained_model():
    model = NeuralNetwork(input_size=784, hidden_size=128, output_size=10)
    weights = np.load('backend/model_weights.npz')
    model.layer1.weights = weights['layer1_weights']
    model.layer1.biases = weights['layer1_biases']
    model.layer2.weights = weights['layer2_weights']
    model.layer2.biases = weights['layer2_biases']
    return model
