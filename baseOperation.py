
import numpy as np
#print(len(matrix[0])) To print Columns number
def remplir_matrice(matrice):
   for i in range(0,len(matrice)):
       for j in range(len(matrice[0])):
           print('M[',i,']','[',j,'] = ',end='')
           matrice[i,j]=float(input())




def vector_init(n):
    print('----------------')
    V = np.zeros(3)
    i = 0
    while i < n:
     print('V[', i, '] = ',end='')
     V[i] = int(input())
     i = i+1
    print('----------------')
    return V




def matrixP(matrix):
    # print(len(matrix)) == Size of matrix
    r=len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i!=len(matrix)-1 and matrix[i][j] == matrix[i][i + 1]: # index is alwys -1 from size cuz we start with 0 i cant on the edge  cuz condition is fals for i+1
                matrix[i, j]=pow(r-i*i, 2)/r*r
            if matrix[i][j]==matrix[i][i-1]:
                matrix[i,j]=pow(i,2)/pow(r,2)
            if matrix[i][j] == matrix[i][i]:
                matrix[i, j] = 2*i*(r-i)/r*r
            else : matrix[i][j] = 0
