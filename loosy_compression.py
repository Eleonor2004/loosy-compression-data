import numpy as np
import matplotlib.pyplot as plt

# Define the number of vectors and their length
num_vectors = 50
vector_length = 10
#Initial data to be compressed
X = np.random.randn(vector_length, num_vectors)
#Calculating the matrix M= X.X(T)
X_transpose = X.T
M = X @ X_transpose
#Calculating D
# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(M)
# Sort together by eigenvalues (descending order)
sorted_results = sorted(zip(eigenvalues, eigenvectors.T), key=lambda x: abs(x[0]), reverse=True)

# Select the l largest eigenvalues and corresponding eigenvectors
l = 2  
largest_eigenvalues = [x[0] for x in sorted_results[:l]]
corresponding_eigenvectors = np.array([x[1] for x in sorted_results[:l]])
D = corresponding_eigenvectors
D_transpose = D
# if X.shape[1] != D_transpose.shape[0]:
#   raise ValueError("Incompatible matrix dimensions for multiplication. X columns must equal D rows.")
C = np.einsum('ij,jk->ik', D_transpose, X)
#The compressed form C of our initial data(X) is C
print("Initial data",X)
print("Compressed data",C)
#Reverting the compressed data to the initial data
X_approximate = D.T @ C
print("Initial data",X)
print("Reverted data",X_approximate)

#Calulation of error and representation
error = np.abs(X_approximate - X)
print("errors", error)
total_error = np.sum(error)
# Select a vector for visualization (replace with desired index)
vector_index = 0
approx_vector = X_approximate[vector_index, :]
original_vector = X[vector_index, :]
# Plot the vectors and their difference
plt.plot(approx_vector, label='Approximated Vector')
plt.plot(original_vector, label='Original Vector')
#plt.plot(error[vector_index, :], label='Absolute Difference (Error)')
plt.xlabel('Vector Dimension')
plt.ylabel('Vector Value')
plt.title('Comparison of Vector ' + str(vector_index + 1))
plt.legend()
plt.grid(True)
plt.show()

print("Total error between matrices:", total_error)


