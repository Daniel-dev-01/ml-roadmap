import numpy as np

# 1. Creating NumPy arrays
scores = np.array([75, 82, 68, 90, 88])

print("Scores:", scores)

# 2. Basic array operations
print("Scores + 5:", scores + 5)
print("Scores * 2:", scores * 2)

# 3. Indexing and slicing
print("First score:", scores[0])
print("First three scores:", scores[:3])

# 4. Useful statistics
print("Mean:", np.mean(scores))
print("Maximum:", np.max(scores))
print("Minimum:", np.min(scores))
print("Standard deviation:", np.std(scores))

# 5. Creating a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatrix:")
print(matrix)

# 6. Shape and reshape
print("Matrix shape:", matrix.shape)

reshaped = matrix.reshape(3, 2)
print("Reshaped matrix:")
print(reshaped)