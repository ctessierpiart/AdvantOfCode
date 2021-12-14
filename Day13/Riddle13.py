import numpy as np
import matplotlib.pyplot as plt
import time

List_of_points = []
List_of_folds = []

with open('Day13/Sheet.csv', 'r') as file:
    line = file.readline()
    while (line) != '\n':
        line = line.strip('\n')
        line = line.split(',')
        coord = [int(line[0]), int(line[1])]
        List_of_points.append(coord)
        line = file.readline()
    for line in file:
        line = line.strip('\n')
        line = line.replace('fold along ', '')
        line = line.split('=')
        List_of_folds.append([line[0], int(line[1])])
        
        
start_time = time.time()        
# Part 1
FirstFold = List_of_folds[0]
List_of_points_1 = List_of_points
if FirstFold[0] == 'x':
    for point in List_of_points_1:
        if point[0] > FirstFold[1]:
            point[0] -= 2*(point[0] - FirstFold[1]) 
else:
    for point in List_of_points_1:
        if point[1] > FirstFold[1]:
            point[1] -= 2*(point[1] - FirstFold[1])

unique_point = []
sum_point = 0
for point in List_of_points_1:
    if point not in unique_point:
        unique_point.append(point)
        sum_point += 1
        
print(f'Points :  {sum_point}')

print(f'Temps execution : {time.time() - start_time}')

start_time = time.time()
# Part 2
List_of_points_2 = List_of_points
for fold in List_of_folds:
    match fold[0]:
        case 'x':
            for point in List_of_points_2:
                if point[0] > fold[1]:
                    point[0] -= 2*(point[0] - fold[1]) 
        case 'y':
            for point in List_of_points_2:
                if point[1] > fold[1]:
                    point[1] -= 2*(point[1] - fold[1])
                    
Display = np.zeros([39, 6]).astype(np.bool_)
for point in List_of_points_2:
    Display[point[0], point[1]] = 1

plt.imshow(Display.T)
print(f'Temps execution : {time.time() - start_time}')
plt.show()