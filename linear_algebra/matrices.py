import numpy as np

A= np.array([[1, 2],
    [3, 4]])

B= np.array([[5, 6],
    [7, 8]])

# Matrix addition
print("A + B:")
print(A + B)

# Matrix multiplication
print("A @ B:")
print(A @ B)

# Transpose
print("Transpose of A:")
print(A.T)

print("Transpose of B:")
print(B.T)

# Determinant
print("Determinant of A:")
print(np.linalg.det(A))

print("Determinant of B:")
print(np.linalg.det(B))