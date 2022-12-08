
import numpy as np
#print(len(matrix[0])) To print Columns number
def remplir_matrice(matrice):
   for i in range(0,len(matrice)):
       for j in range(len(matrice[0])):
           print('M[',i,']','[',j,'] = ',end='')
           matrice[i,j]=float(input())
   print('----------------')



def vector_init(n):
    print('Enter the probability vector of the state : ')
    V = np.zeros(n)
    i = 0
    while i < n:
     print('π [', i, '] = ',end='')
     V[i] = int(input())
     i = i+1
    print('----------------')
    return V

def matrixP(matrix):
    # print(len(matrix)) == Size of matrix
    r=len(matrix)
    r=3
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
