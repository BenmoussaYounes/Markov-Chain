from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from scipy.sparse import csr_matrix



def classify(Matrix):
    Class = {'recurrent': [], 'transient': []}
    graph = csr_matrix(Matrix)
    transient_check = True
    print('Graph : ')
    print(graph)
    cmp = connected_components(Matrix, connection='strong', return_labels=True)
    cmp_list=cmp[1]
    print()
    print('Number of connected component  : ', cmp[0],'/ Matrix Labels : ', cmp[1]) # (of the connected components)
    print('--------------------------------------------------------------')
    checkedIndx=[]
    for i in range(len(cmp_list)):
        state = cmp_list[i]
        exisit=check_if_exisit(checkedIndx, state)
        if exisit == False :
            print('--> The Class Index doest not exist in checked index classes')
            checkedIndx.append(state)
            indix = getClassMemebers(state, cmp_list)
            transient_check =check(Matrix,indix)
            #print('TRANS CHECK BOOL RESULT : ', transient_check)
            if transient_check == True:
                print('Adding in', indix, 'To the Transient Class members')
                Class['transient'].append(indix)
            # elif len(indix) != 1:
            else:
                print('Adding in', indix, 'To the recurrent Class members')
                Class['recurrent'].append(indix)
        print('-------------------------------------')

    print('Recurrent Class : ', Class['recurrent'])
    print('transient Class : ', Class['transient'])






def check_if_exisit(checkedList, state):
    print('Class Index : ', state)
    print('Checked Class Index :', checkedList)
    exisit = False
    if len(checkedList) != 0:
        for i in range(len(checkedList)):
           # print('--> checked List', checkedList[i])
            if checkedList[i] == state :
                print('Already Checked Class ! ')
                exisit = True
   # print('Exist : ', exisit)
    return exisit






def getClassMemebers(state,cmpList):
    classMemebers = []
    for i in range(len(cmpList)):
        if state == cmpList[i]:
            classMemebers.append(i)
    print('--> Class Memebers Index are : ', classMemebers)
    return classMemebers



def check(matrix, Class):
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
            # bah n parcor probality [ 1 0 1 ]
            #print('start')
            #trans_check = True
            print('Probs : ', state[j])
            #print('transfond',transFond)
            if state[j] != 0 and transFond == False:
             intersection = j in Class
             #print('Intersection ', intersection)
             if intersection == True:
             # print('RECURRENT')
              trans_check = False
             if intersection == False:
             # print('TRANSIENT')
              trans_check = True
             if trans_check == True:
              #print('DONE')
              transFond = True
              break


  print('--> Tran Check ! ', trans_check,end='')
  if trans_check != False:
     print(', This Class ', Class, 'is Transient !  ')
  else :
   print(', This Class ', Class,'is Recurrent !  ')
     #print('here: ',matrix[indix][i])
  return trans_check

