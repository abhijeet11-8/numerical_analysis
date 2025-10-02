import numpy as np
import numpy.linalg as la

# Read matrix from input file
with open("A.txt" , "r") as f :
    lines = f.readlines()

# Convert file contents to numpy array
A = np.array([[ float(num)for num in line.split ()] for line in lines ], dtype=np.float32)
print ( "Matrix A :" , A )

print("determinant",la.det(A))
print("rank",la.matrix_rank(A))
print("eigvals",la.eigvals(A))
print("eig",la.eig(A))
# if np.isclose(la.det(A), 0): print(la.inv(A))
# else: print("singular matrix")

# Read matrix from input file
with open("B.txt" , "r") as f :
    lines = f.readlines()

# Convert file contents to numpy array
B = np.array([[ float(num)for num in line.split ()] for line in lines ], dtype=np.float32)
print ( "Matrix B :" , B )

print(A-B)
print(A+B)
print(A*B)
print(A@B)
print(A/B)
print(A**2)