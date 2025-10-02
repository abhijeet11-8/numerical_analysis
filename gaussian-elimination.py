import numpy as np
import numpy.linalg as la

rng = np.random.default_rng(seed=42)
A = rng.random((3,3))
print("A: \n",A)

def gausselimnite(A):
    s = 0
    rank = la.matrix_rank(A)
    for i in range(rank):
        if A[i, i] == 0:
            A[i, i] = 0.5
            s = s + 1
        for j in range(i+1,rank,1):
            m = A[j,i]/A[i,i]
            A[j,] = A[j,] - m * A[i,]
    return(A, s)

a, s = gausselimnite(A)
print("\n eliminated \n",a)
print("\n s = ",s)
