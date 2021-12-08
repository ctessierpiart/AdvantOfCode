import numpy as np
from numpy.core.fromnumeric import cumsum
import matplotlib.pyplot as plt

with open('Day7/Crabs.csv') as file:
    for line in file:
        line = line.strip()
        line = line.split(',')
        Crabs = [int(x) for x in line]
        Crabs = np.array(Crabs)

Min_pos = np.median(Crabs)

Cost = 0
for crab in Crabs:
    Cost += abs(crab - Min_pos)
    
print(f'Crabs first position is {int(Min_pos)} and the total cost is {int(Cost)}')

Cumulative_cost = []
for i in range(max(Crabs)+1):
    if i == 0:
        Cumulative_cost.append(0)
    else:
        Cumulative_cost.append(Cumulative_cost[-1] + i)
        
Costs = []
for pos in range(min(Crabs), max(Crabs)):
    Cost = 0
    for crab in Crabs:
        Cost += Cumulative_cost[abs(crab-pos)]
    Costs.append(Cost)
        
Min_Cost = min(Costs)
Min_Pos = Costs.index(Min_Cost)
print(f'Crab second position is {Min_Pos} and its total cost is {Min_Cost}')