import numpy as np

# Two vectors
a = np.array([3, 4])
b = np.array([1, 2])

# Vector addition
addition = a + b
print("Addition:", addition)

# Vector subtraction
subtraction = a - b
print("Subtraction:", subtraction)

# Scalar multiplication
scaled = 2 * a
print("Scaled:", scaled)

# Dot product
dot_product = np.dot(a, b)
print("Dot product:", dot_product)

# Magnitude
magnitude = np.linalg.norm(a)
print("Magnitude of a:", magnitude)

# Linear combination
a = np.array([2, 1])
b = np.array([1, 3])

linear_combination = 3 * a + 2 * b
print("Linear combination:", linear_combination)