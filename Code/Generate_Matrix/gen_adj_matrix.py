import numpy as np

# Generate a random 100x100 matrix
size =100
matrix = np.random.randint(0, 2, (size, size))

# Generate the adjacency matrix
adjacency_matrix = np.zeros((size*size, size*size), dtype=int)

for i in range(size):
    for j in range(size):
        # Find the indices of adjacent cells
        above = (i-1)*size + j
        below = (i+1)*size + j
        left = i*size + (j-1)
        right = i*size + (j+1)

        # Check if adjacent cells exist and set adjacency matrix accordingly
        if i > 0 and matrix[i-1][j] == 1:
            adjacency_matrix[i*size+j][above] = 1
        if i < size-1 and matrix[i+1][j] == 1:
            adjacency_matrix[i*size+j][below] = 1
        if j > 0 and matrix[i][j-1] == 1:
            adjacency_matrix[i*size+j][left] = 1
        if j < size-1 and matrix[i][j+1] == 1:
            adjacency_matrix[i*size+j][right] = 1

print(adjacency_matrix.shape)
# Save the adjacency matrix to a text file
np.savetxt("adj_matrix.txt", adjacency_matrix, fmt="%d")

# Print a message indicating the file has been saved
print("The adjacency matrix has been saved to adj_matrix.txt.")
