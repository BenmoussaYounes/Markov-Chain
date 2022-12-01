from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from scipy.sparse import csr_matrix

def classify(Matrix):
    Class = {'recurrent': [], 'transient': []}
    graph = csr_matrix(Matrix)
    transient_check=True
    print('Graph : ')
    print(graph)
    cmp = connected_components(Matrix, connection='strong', return_labels=True)
    cmp_list=cmp[1]
    print('Number of connected component  : ', cmp[0],'/ Matrix Labels : ', cmp[1]) # (of the connected components)
    print('---------------')
    for i in range(len(cmp_list)):
        temp=cmp_list[i]
        print(' temp : ', temp)
        print('i',i )
        indix = []
        sameIndix = exisitClass(Class['transient'], Class['recurrent'], temp)
        if sameIndix == False :
         indix.append(i)
         for j in range(len(cmp[1])-1):
             print(' cmp_list[j] : ', cmp_list[j])
             #if j==i:
             #  continue

             if temp== cmp_list[j]:
                 #print('down here sir')
                 indix.append(j)
         transient_check=check(Matrix,indix)
         print('TRANS CHECk',transient_check)
         if transient_check == True:
          Class['transient'].append(indix)
         #elif len(indix) != 1:
         else:
          print('adding in',indix)
          Class['recurrent'].append(indix)

    print('Recurrent Class : ', Class['recurrent'])
    print('transient Class : ', Class['transient'])



def exisitClass(tranClass,reclass,state):
   print('State',state)
   print('traClass',tranClass)
   print('recClass',reclass)
   exisit = False
   if len(tranClass) != 0:
      for t in range(len(tranClass)):
       print('--> t', tranClass[t])
       if  tranClass[t] == state and len(tranClass) != 0:
                   print('SAME INDEX ! ')
                   exisit=True
   if len(reclass) != 0:
      for t in range(len(reclass)):
       print('--> t', reclass[t])
       if len(reclass) != 0 and reclass[t] == state :
                   print('SAME INDEX ! ')
                   exisit=True
   print('Exisit',exisit)
   return exisit

def check(matrix, Class):
  print('Class : ', Class)
  trans_check=False
  for i in range(len(matrix[Class])):
    state=matrix[Class][i]
    print('I', Class[i])
    print('State_probs : ', state)
    for ClassElm in Class:
             for j in range(len(state) - 1):
               if state[j] != 0 and j != ClassElm:
                 for k in Class:
                  if j != k:
                   print('Transient')
                   #print('Class element check : ', k)
                   #print('state number = ClassElm value')
                   #print('state number   -->', j)
                   #print('ClassElm value -->', ClassElm)
                   trans_check = True
                  else:
                   print('Class element check : ', k)
                   print('state number   -->', j)
                   print('ClassElm value -->', ClassElm)
                   trans_check = False


  if trans_check != False:
     print('This Class is Transient !  ', Class)
  else :
   print('This Class is Recurrent !  ', Class)
     #print('here: ',matrix[indix][i])
  return trans_check

def check(matrix, Class):
  print('Class : ', Class)
  transFond = False
  trans_check=True
  for i in range(len(matrix[Class])):
      if transFond == False:
          state=matrix[Class][i]
          print('-> I : ', Class[i])
          print('State_probs : ', state)

          length=len(Class)
          trans_check = True
          for j in range(len(state)):
            # bah n parcor probality [ 1 0 1 ]
            print('start')
            #trans_check = True
            print('Probs',state[j])
            print('transfond',transFond)
            if state[j] != 0 and transFond == False:
             print('--> state probs',state[j])
             b=j in Class
             print('result b ',b)
             if b == True:
              print('RECURRENT')
              trans_check = False
             if b == False:
              print('TRANSIENT')
              trans_check = True
             if trans_check == True:
              print('DONE')
              transFond = True
              break


  print('tran Check', trans_check)
  if trans_check != False:
     print('This Class is Transient !  ', Class)
  else :
   print('This Class is Recurrent !  ', Class)
     #print('here: ',matrix[indix][i])
  return trans_check
