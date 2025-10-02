import numpy as np
import numpy.linalg as la

rng = np.random.default_rng(seed=42)
A = rng.random((3,3))
print("A: \n",A)

def vect(A):
    v = np.array([])
    r,c = A.shape
    for i in range(r):
        v[i,] = A[i,i]
    return v

print(vect(A))
