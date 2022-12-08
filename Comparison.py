from Simulation import simulation
from transMatrix import StationnarystateVector
class comparison:

 def comparison_Analytical_Empirical_Methods(self,Matrix,pi):
     print('Empirical prob : ')
     s = simulation()
     s.PDOS_Simulation(Matrix[0], s.RandomWalk(Matrix, 0))
     print('Analytical prob : ')
     StationnarystateVector(Matrix, pi)