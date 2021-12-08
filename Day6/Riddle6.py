import numpy as np
import time

with open('Day6/LanternFish.csv') as file:
    for line in file:
        line = line.strip()
        line = line.split(',')
        LanternFish = [int(x) for x in line]
        LanternFish = np.array(LanternFish)
        
start_timer = time.time()

Number_of_cycle = 256

Fish_by_day = np.array([sum(LanternFish == 8),
               sum(LanternFish == 7),
               sum(LanternFish == 6),
               sum(LanternFish == 5),
               sum(LanternFish == 4),
               sum(LanternFish == 3),
               sum(LanternFish == 2),
               sum(LanternFish == 1),
               sum(LanternFish == 0)])
Fish_by_day = Fish_by_day.astype(np.uint64)

for cycle in range(Number_of_cycle):
    Fish_by_day = np.insert(Fish_by_day, 0, Fish_by_day[8], axis = 0)
    Fish_by_day[2] += Fish_by_day[9]
    Fish_by_day = Fish_by_day[:9]

print(f'Cycle = {cycle}; Nombre de poisson = {sum(Fish_by_day)}')
print(time.time() - start_timer)