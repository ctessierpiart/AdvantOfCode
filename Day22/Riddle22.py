import numpy as np
from dataclasses import dataclass
from collections import namedtuple

Initialisation = []
Boot_sequence = []

@dataclass
class Command:
    state : str
    x_beg : int
    x_end : int
    y_beg : int
    y_end : int
    z_beg : int
    z_end : int
    
Drive_size = 101
offset = 51
Drive = np.zeros([Drive_size, Drive_size, Drive_size]).astype(np.bool_)

x_max, y_max, z_max, x_min, y_min, z_min = 0, 0, 0, 0, 0, 0

with open('Day22/Boot.txt') as file:
    for line in file:
        line = line.strip('\n')
        state, coord = line.split(' ')
        x_string, y_string, z_string = coord.split(',')
        x = [int(coord) for coord in x_string.removeprefix('x=').split('..')]
        y = [int(coord) for coord in y_string.removeprefix('y=').split('..')]
        z = [int(coord) for coord in z_string.removeprefix('z=').split('..')]
        local_command = Command(state, min(x), max(x), min (y), max(y), min(z), max(z))
        is_init = True
        for element in x+y+z:
            if abs(element) > 50:
                is_init = False
        if is_init:
            Initialisation.append(local_command)
        Boot_sequence.append(local_command)
        if max(x) > x_max:
            x_max = max(x)
        if max(y) > y_max:
            y_max = max(y)
        if max(z) > z_max:
            z_max = max(z)
        if min(x) > x_min:
            x_min = min(x)
        if min(y) > y_min:
            y_min = min(y)
        if min(z) > z_max:
            z_min = min(z)

for command in Initialisation:
    Drive[command.x_beg+offset:command.x_end+offset+1,
          command.y_beg+offset:command.y_end+offset+1,
          command.z_beg+offset:command.z_end+offset+1] = (command.state == 'on')

print(f'Solution 1 : {sum(sum(sum(Drive)))}')

def check_for_overlap(cub_1 : Command, cub_2 : Command):
    overlap_sum = 0
    x_overlap = (cub_2.x_beg <= cub_1.x_beg <= cub_2.x_end) or (cub_2.x_beg <= cub_1.x_end <= cub_2.x_end) or (cub_1.x_beg <= cub_2.x_beg <= cub_1.x_end) or (cub_1.x_beg <= cub_2.x_end <= cub_1.x_end)
    y_overlap = (cub_2.y_beg <= cub_1.y_beg <= cub_2.y_end) or (cub_2.y_beg <= cub_1.y_end <= cub_2.y_end) or (cub_1.y_beg <= cub_2.y_beg <= cub_1.y_end) or (cub_1.y_beg <= cub_2.y_end <= cub_1.y_end)
    z_overlap = (cub_2.z_beg <= cub_1.z_beg <= cub_2.z_end) or (cub_2.z_beg <= cub_1.z_end <= cub_2.z_end) or (cub_1.z_beg <= cub_2.z_beg <= cub_1.z_end) or (cub_1.z_beg <= cub_2.z_end <= cub_1.z_end)
    if x_overlap and y_overlap and z_overlap:
        sorted_x = [cub_1.x_beg, cub_1.x_end, cub_2.x_beg, cub_2.x_end].sort()
        sorted_y = [cub_1.y_beg, cub_1.y_end, cub_2.y_beg, cub_2.y_end].sort()
        sorted_z = [cub_1.z_beg, cub_1.z_end, cub_2.z_beg, cub_2.z_end].sort()
        overlap_sum = (sorted_x[1] - sorted_x[2]) * (sorted_y[1] - sorted_y[2]) * (sorted_z[1] - sorted_z[2])
    return overlap_sum
    
    
    

sum = 0
processed_cuboid = []
for command in Boot_sequence:
    new_cubes = (command.x_end-command.x_beg)*(command.y_end-command.y_beg)*(command.z_end-command.z_beg)*(command.state == 'on')
    for cuboid in processed_cuboid:
        pass
    processed_cuboid.append(command)