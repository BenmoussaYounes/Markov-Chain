import numpy as np


class markovChain:
 def transitionMatrice_check(self,matrix, vector):
    #Vector de probability initial
    line_sum=0
    for i in range(len(vector)):
        line_sum=line_sum+vector[i]
        if i==len(vector)-1 :
            if line_sum == 1:
             print('--> The  Vector is valid, line sum is equal to 1')
            else:
             print('--> invalid Vector !, line sum is not equal to 1')

    valid = True
    for i in range(len(matrix)):
       line_sum=0
       for j in range(len(matrix)):
           if (matrix[i][j] > 1) or (matrix[i][j] < 0):
             print('--> Value of elements must be between (0,1) !','M[',i,']','[',j,']','= ',matrix[i][j])
             valid = False
             break
           line_sum=line_sum+matrix[i][j]  #to check the line sum value
           #print('line sum : ', line_sum)
           if j==len(matrix)-1 and line_sum !=1:
               print('--> the line sum is not equal to 1 !')
               valid=False
               break

       if not valid:
           break
    if valid: print('--> The matrix given is a Valid transition matrix')
    else: print('--> The matrix given is not a Valid transition matrix ! ')
    print('----------------')



 def TransitionProbability_of_n_steps(self,matrix, v):
  n = int(input('Enter the number of steps : '))
  i=0
  while(i<n):
      matrix = np.dot(matrix, matrix)
      i=i+1
  v = np.dot(v, matrix)
  print(v)
  print('-------------------')




 def StationnarystateVector(self,matrix, v):
  i=0
  n=50
  while(i<n):
      v = np.dot(v, matrix)
      #print('π ',i,' = ', v)
      i=i+1
  #print('Stationnary State Vector : ')
  print('π = ', v)
  print('----------------')

