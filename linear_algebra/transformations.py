import numpy as np

# A vector
v = np.array([2, 1])

# Transformation matrix
A = np.array([
    [1, 1],
    [0, 1]
])

# Apply transformation
transformed = A @ v

print("Original vector:", v)
print("Transformed vector:", transformed)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)