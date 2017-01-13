# # Linear Algebra

# Import Relevant Libraries
import numpy as np

# Define Variables
A = np.matrix([[1, 2, 3],[2, 7, 4]])
B = np.matrix([[1, -1],[0, -1]])
C = np.matrix([[5, -1],[9, 1],[6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])

u = np.matrix([6, 2, -3, 5])
v = np.matrix([3, 5, -1 ,4])
w = np.matrix([1,8, 0, 5]).transpose()

# ## Part 1: Matrix Dimensions
# 1.1
print('Dimension of A:',np.shape(A))
# 1.2
print('Dimension of B:',np.shape(B))
# 1.3
print('Dimension of C:',np.shape(C))
# 1.4
print('Dimension of D:',np.shape(D))
# 1.5
print('Dimension of u:',np.shape(u))
# 1.6
print('Dimension of w:',np.shape(w))


# # Part 2: Vector Operations
# Define Variables
alpha = 6

# 2.1 
print('u + v =', u + v)
# 2.2
print('u - v =', u - v)
# 2.3
print('alpha * u =', alpha * u)
# 2.4
print('u * v =', int(u * v.transpose()))
# 2.5
print('||u|| =', np.linalg.norm(u))


# # Part 3: Matrix Operations
# 3.1
print('A + C = Not Defined')
# 3.2
print("A - C'=", A - C.transpose())
# 3.3
print("C' + 3D =", C.transpose() + 3*D)
# 3.4
print('BA =',B*A)
# 3.5
print("BA' = Not Defined")
# 3.6
print("BC = Not Defined")
# 3.7
print("CB =", C*B)
# 3.8
print("B^4 =",B^4)
# 3.9
print("AA' =",A*A.transpose())
# 3.10
print("D'D =",D.transpose()*D)

