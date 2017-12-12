import numpy as np

class Network:
    def __init__(self):
        self.input_size = 3
        self.hidden_size = 4
        self.output_size = 1
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)
        self.fitness = 0

    def forward(self, inputs):
        self.z2 = np.dot(inputs, self.W1)
        self.a2 = np.tanh(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = np.tanh(self.z3)
        return yHat

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
