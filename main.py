import Simulation
import networkx as nx
import numpy as np

from classification import classify
from baseOperation import remplir_matrice, vector_init, matrixP
from transMatrix import transitionMatrice_check, StationnarystateVector
from Comparison import comparison

from itertools import accumulate



#matrixP(matrix)
#Ex1
B=np.array([[0.2,0.5,0.3],[0,0.5,0.5],[0.3,0.4,0.3]])
#B=np.array([[0.5,0.6,0,5,6,8],[0.5,0.6,0,5,6,8],[0.5,0.6,0,5,6,8],[0.5,0.6,0,5,6,8],[0.5,0.6,0,5,6,8],[0.5,0.6,0,5,6,8]])
#B=np.array([[1,0,0,0],[1,0,1,0],[0,1,0,1],[0,0,0,1]])
#B=np.array([[0.5,0.5,0,0],[0,0.5,0.5,0],[0,0.5,0,0.5],[0.5,0.5,0,0]])
print('Transition Matrix : ')
print(B)
pi=vector_init(len(B[0]))
transitionMatrice_check(B, pi)
c=comparison()
c.comparison_Analytical_Empirical_Methods(B,pi)
#print(B)
#classify(B)
#r=int(input("Enter The matrix size  : "))



#matrix = np.zeros((r,r)) # Pre-allocate matrix
#matrixP(matrix)
#remplir_matrice(matrix)

#print(matrix)

#Ex2
#print('transition matrix check : ')
#transitionMatrice_check(matrix, pi)
#StationnarystateVector(matrix, pi)






#VtransationProbalities(matrix, pi)
#B=np.array(matrix)
#G = nx.from_numpy_array(B)
''''
print('Is Connected : ', nx.is_connected(G))
for edge in G.edges:
    print(edge)
options = {
    'node_color': 'blue',
    'node_size': 250,
    'width': 2,
    'arrowstyle': '-|>',
    'arrowsize': 7,
}
comp = list(nx.strongly_connected_components(G))
'''
#nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)

#nx.draw_networkx_edge_labels(G, pos, edge_labels)
#nx.strongly_connected_components(B)
#nx.connected_components()

'''''
pos=nx.spring_layout(G)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos)
nx.draw(G, with_labels=True,pos=pos)


plt.show()
'''

'''''
              for ClassElmIndix in range(len(Class)):
                  print('j',j)
                  print('ClasseELmind',Class[ClassElmIndix])
                  if j == Class[ClassElmIndix]:
                      print('RECURRENT')
                      trans_check=False
              if trans_check == True :
                 print('DONE') 
                 break 
    for ClassElm in Class:
             print('Class ELM', ClassElm)
             if transFond == False :
              for j in range(len(state)):
                #print('state j ', state[j])
                #print('j', j)
                 # Check if tran class with all nightbor states class element are same class state
                if state[j] != 0 and j != ClassElm:
                    print('here')
                    #print('tran')
                   #print('state number   -->', j)
                    #print('ClassElm value -->', ClassElm)
                    print('switched')
                    transFond = True
                    trans_check = True
                else:
                    #print('rec')
                     #print('state number   -->', j)
                   #print('ClassElm value -->', ClassElm)
                   trans_check = False
                   #break
    '''''


