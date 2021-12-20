import numpy as np

with open('Day15/Cave.csv', 'r') as file:
    Cave_string = file.read()
    Cave_string = Cave_string.split('\n')
    Cave = []
    for line in Cave_string:
        line = [int(risk) for risk in line]
        Cave.append(line)
    Cave = np.array(Cave)
    
def find_shortest_neighbour(Distance_to_source, x_step : int, y_step : int):
    y_up = y_step - 1 * (y_step > 0)
    y_down = y_step + 1 * (y_step < Size_y-1)
    x_right = x_step + 1 * (x_step < Size_x-1)
    x_left = x_step - 1 * (x_step > 0)
    
    Dist_up = Distance_to_source[y_up, x_step]
    Dist_down = Distance_to_source[y_down, x_step]
    Dist_right = Distance_to_source[y_step, x_right]
    Dist_left = Distance_to_source[y_step, x_left]
    
    Dists = np.array([Dist_up, Dist_down, Dist_right, Dist_left])
    
    match np.argmin(Dists):
        case 0:
            return [y_up, x_step]
        case 1:
            return [y_down, x_step]
        case 2:
            return [y_step, x_right]
        case 3:
            return [y_step, x_left]
        
def update_line(Distance_to_source, Predecessor, step):
    x_step = step
    y_step = 0
    
    Updated = False
    end_zone = False
    if step == 0:
        end_zone = True
    while not end_zone:
        if not ((x_step > Size_x - 1) or (y_step > Size_y - 1)):
            Predecessor[y_step, x_step] = find_shortest_neighbour(Distance_to_source, x_step, y_step)
            pred_dist = Distance_to_source[Predecessor[y_step, x_step][0], Predecessor[y_step, x_step][1]]
            prev_dist = Distance_to_source[y_step, x_step]
            Distance_to_source[y_step, x_step] = Cave[y_step, x_step] + pred_dist
            if prev_dist != Distance_to_source[y_step, x_step]:
                Updated = True
        if y_step == step:
            end_zone = True
        x_step -= 1
        y_step += 1
        
    return Updated
      
# Cave = np.array([[1,1,6,3,7,5,1,7,4,2],
# [1,3,8,1,3,7,3,6,7,2],
# [2,1,3,6,5,1,1,3,2,8],
# [3,6,9,4,9,3,1,5,6,9],
# [7,4,6,3,4,1,7,1,1,1],
# [1,3,1,9,1,2,8,1,3,7],
# [1,3,5,9,9,1,2,4,2,1],
# [3,1,2,5,4,2,1,6,3,9],
# [1,2,9,3,1,3,8,5,2,1],
# [2,3,1,1,9,4,4,5,8,1]])
    
# Part 1

Size_y, Size_x = Cave.shape    
Shape_predecessor = (Size_y, Size_x, 2)
max_distance = Size_x + Size_y

Distance_to_source = np.zeros(Cave.shape).astype(np.int32)
Distance_to_source.fill(np.iinfo(np.int32).max)
Predecessor = np.zeros(Shape_predecessor).astype(np.int32)
Predecessor.fill(0)

Distance_to_source[0,0] = 0

for step in range(max_distance):
    update_line(Distance_to_source, Predecessor, step)
    
    update_step = step - 1
    while update_step > 0:
        is_updated = update_line(Distance_to_source, Predecessor, update_step)
        if is_updated == True:
            update_step = step
        update_step -= 1
        
print(Distance_to_source)

# Part 2
for i in range(5):
    new_tile = Cave + i
    new_tile[new_tile > 9] -= 9
    new_line = new_tile
    for j in range(1,5):
        new_tile = new_tile + 1
        new_tile[new_tile > 9] -= 9
        new_line = np.append(new_line, new_tile, axis = 0)
    if i == 0:
        new_cave = new_line
    else:
        new_cave = np.append(new_cave, new_line, axis = 1)
Cave = new_cave

Size_y, Size_x = Cave.shape    
Shape_predecessor = (Size_y, Size_x, 2)
max_distance = Size_x + Size_y

Distance_to_source = np.zeros(Cave.shape).astype(np.int32)
Distance_to_source.fill(np.iinfo(np.int32).max)
Predecessor = np.zeros(Shape_predecessor).astype(np.int32)
Predecessor.fill(0)

Distance_to_source[0,0] = 0

for step in range(max_distance):
    update_line(Distance_to_source, Predecessor, step)
    
    update_step = step - 1
    while update_step > 0:
        is_updated = update_line(Distance_to_source, Predecessor, update_step)
        if is_updated == True:
            update_step = step
        update_step -= 1
    print(f'Pourcentage de ligne : {(step+1)/(Size_y + Size_x)*100} %')
        
print(Distance_to_source)