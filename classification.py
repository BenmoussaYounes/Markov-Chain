from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix


class classfication:

 def classify(self, Matrix):
    Class = {'recurrent': [], 'transient': []}
    graph = csr_matrix(Matrix)
    print('Graph : ')
    print(graph)
    cmp = connected_components(Matrix, connection='strong', return_labels=True)
    cmp_list=cmp[1]
    print()
    print('Number of connected component  : ', cmp[0], '/ Matrix Labels : ', cmp[1])  # (of the connected components)
    print('--------------------------------------------------------------')
    checkedIndx=[]
    for i in range(len(cmp_list)):
        state = cmp_list[i]
        exisit=self.check_if_exisit(checkedIndx, state)
        if exisit == False :
            print('--> The Class Index doest not exist in checked index classes')
            checkedIndx.append(state)
            indix = self.getClassMemebers(state,cmp_list)
            transient_check =self.check(Matrix,indix)
            if transient_check == True:
                print('Adding in', indix, 'To the Transient Class members')
                Class['transient'].append(indix)
            else:
                print('Adding in', indix, 'To the recurrent Class members')
                Class['recurrent'].append(indix)
        print('-------------------------------------')

    print('Recurrent Class : ', Class['recurrent'])
    print('transient Class : ', Class['transient'])


 def check_if_exisit(self,checkedList, state):
    print('Class Index : ', state)
    print('Checked Class Index :', checkedList)
    exisit = False
    if len(checkedList) != 0:
        for i in range(len(checkedList)):
            if checkedList[i] == state :
                print('Already Checked Class ! ')
                exisit = True
    return exisit


 def getClassMemebers(self,state,cmpList):
    classMemebers = []
    for i in range(len(cmpList)):
        if state == cmpList[i]:
            classMemebers.append(i)
    print('--> Class Memebers Index are : ', classMemebers)
    return classMemebers


 def check(self,matrix, Class):
  print('REC / TRANS Class CHECK --------')
  print('Real States of the Class : ', Class)
  transFond = False
  trans_check=True
  for i in range(len(matrix[Class])):
      if transFond == False:
          state=matrix[Class][i]
          print('-> I : ', Class[i])
          print('State_probs : ', state)
          trans_check = True
          for j in range(len(state)):
            print('Probs : ', state[j])
            if state[j] != 0 and transFond == False:
             intersection = j in Class
             if intersection == True:
              trans_check = False
             if intersection == False:
              trans_check = True
             if trans_check == True:
              transFond = True
              break


  print('--> Tran Check ! ', trans_check,end='')
  if trans_check != False:
     print(', This Class ', Class, 'is Transient !  ')
  else :
   print(', This Class ', Class,'is Recurrent !  ')
  return trans_check

