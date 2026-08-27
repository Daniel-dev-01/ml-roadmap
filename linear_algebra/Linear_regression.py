import numpy as np

# Input data
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

# Target values
y = np.array([
    3,
    5,
    7,
    9,
    11
])

# Model parameters
w = np.array([2])
b = 1

# Predictions
predictions = X @ w + b

print("Predictions:")
print(predictions)

print("\nActual:")
print(y)