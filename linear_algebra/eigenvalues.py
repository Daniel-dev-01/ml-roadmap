import numpy as np
#"Here is a matrix. Find its eigenvalues and eigenvectors. 
# Take each eigenvector and its corresponding eigenvalue. Calculate Av.
#  Calculate λv. Compare them. If they're equal, we've verified that it's actually an eigenvector."
A = np.array([
    [4, 1],
    [0, 4]
])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:")
print(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

# Verify Av = λv
for i in range(len(eigenvalues)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]

    left_side = A @ eigenvector
    right_side = eigenvalue * eigenvector

    print(f"Eigenvalue {i + 1}: {eigenvalue}")
    print("Av:", left_side)
    print("λv:", right_side)
    print("Verified:", np.allclose(left_side, right_side))