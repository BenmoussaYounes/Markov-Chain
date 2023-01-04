import numpy as np


class baseOperation:
 def matrix_init(self, matrix):
   for i in range(0, len(matrix)):
       for j in range(len(matrix[0])):
           print('M[',i,']','[',j,'] = ',end='')
           matrix[i, j]=float(input())
   print('----------------')


 def vector_init(self, n):
    print('Enter the probability vector of the state : ')
    V = np.zeros(n)
    i = 0
    while i < n:
     print('π [', i, '] = ', end='')
     V[i] = int(input())
     i = i+1
    print('----------------')
    return V

 def matrixP(self, matrix):
    # print(len(matrix)) # Size of matrix
    r=len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j==i+1:
                matrix[i][j]=(np.power(r-i, 2))/(np.power(r, 2))
            elif j==i-1:
                matrix[i][j]=(np.power(i, 2))/(np.power(r, 2))
            elif j==i:
                matrix[i][j] = (2*i*(r-i))/(r*r)
            else : matrix[i][j] = 0
    print('----------------')

 def printMatrix(self, matrix):
     print('Transition Matrix : ')
     print(matrix)
     print('----------------')