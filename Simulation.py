from itertools import accumulate
from random import random


class simulation:

 def RandomWalk(self,matrix,position):
  # Matrix (Markov chain) - number of steps - Postion Start state
  #print('state probs',state_prob)
  steps=5000
  path = []
  for i in range(steps):
   path.append(position)
   state_prob = matrix[position]
   #print('position',position)
   #accumulate Return the sum of the list element by element
   generatorList = list(accumulate(state_prob))
   #print('generator LIST', generatorList)
   # Moving to the next position
   position=self.Generator_check(generatorList)

 # print('Visited State after ',steps,'steps are : ',path)
  return (path)

 def Generator_check(self,generatorList):
  rand = random()
  for i in range(len(generatorList)):
    if rand<generatorList[i] :
     #print('Random number : ', rand,'generator check',generatorList[i])
     return i






 def PDOS_Simulation(self,states_number,path):
   v=[]
   for s in range(len(states_number)):
    v.insert(s,path.count(s)/len(path))
   print('π  = ',v)
   print('----------------')

