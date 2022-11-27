import numpy as np


def transitionMatrice_check(matrix, vector):
    #Vector de probability initial
    line_sum=0
    for i in range(len(vector)):
        line_sum=line_sum+vector[i]
        if i==len(vector)-1 :
            if line_sum == 1:
             print('The  Vector is valid, line sum is equal to 1')
            else:
             print('invalid Vector !, line sum is not equal to 1')

    valid = True
    for i in range(len(matrix)):
       line_sum=0
       for j in range(len(matrix)):
           if (matrix[i][j] > 1) or (matrix[i][j] < 0):
             print(' Value of elements must be between (0,1) !','M[',i,']','[',j,']','= ',matrix[i][j])
             valid = False
             break
           line_sum=line_sum+matrix[i][j]# to check the line sum value
           print('line sum : ', line_sum)
           if j==len(matrix)-1 and line_sum !=1:
               print('the line sum is not equal to 1 !')
               valid=False
               break

       if not valid:
           break
    if valid: print('The matrix given is a Valid transition matrix')
    else: print('The matrix given is not a Valid transition matrix ! ')



def VtransationProbalities(matrix,v,n):
  i=0
  while(i<n):
      v=np.dot(v, matrix)
      i=i+1
  print(v)




def ntransationProbalities(matrix,n):
  i=0
  while(i<n):
      matrix=np.dot(matrix,matrix)
      i=i+1
  return  matrix



def mc_Classification(matrix):
    for i in range(len(matrix)):
        recState=False
        transientState=True
        for j in range(len(matrix)):
            print('J',j,'I',i,matrix[j][i])
            if matrix[j][i] != 0 and i != j :
                transientState=False
            if transientState==False:
                print(j, '-->', i,': ',matrix[j][i])
                print('State ', i, ': Is Recurrent')
                print('------------')
                break
            if j == len(matrix)-1:
              print('State ', i, ': Is Transient')
              print('------------------')

