import numpy as np

from markovChain import markovChain
from comparison import comparison
from classification import classfication
from baseOperation import baseOperation


mc = markovChain()
clasify = classfication()
cm = comparison()
b = baseOperation()

size = int(input("Enter The matrix size  : "))

matrix = np.zeros((size, size))  # Pre-allocate matrix
b.matrix_init(matrix)  # matrix = np.array([[1, 0, 0, 0], [1/4, 0, 3/4, 0], [0, 1/3, 0, 2/3], [0, 0, 0, 1]])

b.printMatrix(matrix)

clasify.classify(Matrix=matrix)

pi = b.vector_init(len(matrix[0]))  # pi = [1, 0, 0, 0]

mc.transitionMatrice_check(matrix, pi)

cm.comparison_Analytical_Empirical_Methods(matrix, pi)

