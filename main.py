import networkx as nx
import numpy as np

from classification import classify
from baseOperation import remplir_matrice, vector_init, matrixP
from transMatrix import transitionMatrice_check, mc_Classification,ntransationProbalities
from scipy.sparse.csgraph import connected_components

#matrixP(matrix)
#Ex1

#B=np.array([[0.5,0.6,0],[0,0.5,0.5],[0,0.4,0]])
B=np.array([[1,0,0],[0,0.5,0.5],[1,0.4,0.2]])
classify(B)
r=int(input("Entrer la dimension de la matrice : "))
matrix = np.zeros((r,r)) # Pre-allocate matrix
remplir_matrice(matrix)
print(matrix)
print(connected_components(matrix))
pi=vector_init(r)



#Ex2
print('transition matrix check : ')
transitionMatrice_check(matrix, pi)
n=int(input('Enter the number of steps : '))
ntransationProbalities(matrix,n,pi)

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




