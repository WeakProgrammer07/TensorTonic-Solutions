import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    N, M = A.shape
    A_transpose = np.zeros((M, N))
    for i in range(N):
        for j in range(M):
            A_transpose[j, i] = A[i, j]
    return A_transpose