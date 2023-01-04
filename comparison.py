from simulation import simulation
from markovChain import markovChain

class comparison:

 def comparison_Analytical_Empirical_Methods(self, matrix, pi):
     sim = simulation()
     mc  = markovChain()
     print('Empirical prob : ')
     sim.PDOS_Simulation(matrix[0], sim.RandomWalk(matrix, 0))
     print('Analytical prob : ')
     mc.StationnarystateVector(matrix, pi)