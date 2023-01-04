from itertools import accumulate
from random import random


class simulation:


 def RandomWalk(self,matrix,position):
  # Matrix (Markov chain) - number of steps - Postion Start state
  #print('state probs',state_prob)
  steps=8000
  path = []
  for i in range(steps):
   path.append(position)
   state_prob = matrix[position]
   #print('position',position)
   #accumulate Return the sum of the list element by element
   generatorList = list(accumulate(state_prob))
   #self.tri(generatorList,[])
   #print('generator LIST', generatorList)
   # Moving to the next position
   position=self.Generator_check(generatorList)
   # print('Visited State after ',steps,'steps are : ',path)
  return (path)



 def Generator_check(self,generatorList):
  rand = random()
  #print('rev list ',list(reversed(generatorList)))
 # print('rand',rand)
 # print('Generator List : ',generatorList)
  index=len(generatorList)-1
  while index!=0:
     # print('--> index', index)
      if rand>generatorList[index-1]:
          #print('index', index)
          return index
      index=index-1
      if index==0:
         # print('index', index)
          return index

  '''''
   Basic loop Methode
    for i in range(len(generatorList)):
      # print('i', i)
      # print('gen', generatorList[i])
      if rand < generatorList[i]:
          # print('Random number : ', rand,'generator check',generatorList[i])
          return i
  ----
  '''


 def tri(self, generatorList, newlist):
     index = len(generatorList) - 1
     while index != 0:
         newlist.append(generatorList[index] - generatorList[index - 1])
         print('index', newlist)
         index = index - 1
         if index == 0:
             newlist.append(generatorList[index] - generatorList[index - 1])
             # print('index', index)
             break
     print(newlist)

 def PDOS_Simulation(self,states_number,path):
   v=[]
   for s in range(len(states_number)):
    v.insert(s,path.count(s)/len(path))
   print('π  = ',v)
   print('----------------')

