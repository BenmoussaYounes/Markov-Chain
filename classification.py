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
        indix = []
        indix.append(i)
        for j in range(len(cmp[1])-1):
            if i==j:
             continue
            print(' cmp_list[j] : ', cmp_list[j])
            if temp== cmp_list[j]:
                print('down here sir')
                indix.append(j)
        transient_check=check(Matrix,indix)
        if transient_check == True:
         Class['transient'].append(indix)
        elif len(indix) != 1:
         print('adding in',indix)
         Class['recurrent'].append(indix)

    print('Recurrent Class : ', Class['recurrent'])
    print('transient Class : ', Class['transient'])



def check(matrix, indix):
  print('indix : ', indix)
  trans_check=False
  for i in range(len(matrix[indix])):
     print('here: ',matrix[indix][i])


  return trans_check