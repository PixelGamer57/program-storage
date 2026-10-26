import numpy as np
import math

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input (flattened)
inp = np.array([[0,0,0],
                [0,0,0],
                [0,0,0]])
inp = inp.flatten()  # shape (9,)

out_size = 2
layer_num = 2
layer_height = 4

# Weight shapes:
# Layer 0: 9 → 4
# Layer 1: 4 → 4
# Output: 4 → 2

weights = []
biases = []

# Input → first hidden layer
weights.append(np.ones((layer_height, len(inp))))
biases.append(np.ones(layer_height))

# Hidden layers
for _ in range(layer_num - 1):
    weights.append(np.ones((layer_height, layer_height)))
    biases.append(np.ones(layer_height))

# Output layer
weights.append(np.ones((out_size, layer_height)))
biases.append(np.ones(out_size))

# Forward pass
a = inp
for W, b in zip(weights, biases):
    a = sigmoid(W @ a + b)

print("Network output:", a)
