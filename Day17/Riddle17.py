from math import sqrt, ceil, floor

x_beg = 0
x_end = 0
y_beg = 0
y_end = 0

with open('Day17/Target.txt') as file:
    _, coordonates = file.read().split(': ')
    x_coord, y_coord = coordonates.split(', ')
    x_coord = x_coord.strip('x=').split('..')
    y_coord = y_coord.strip('y=').split('..')
    x_beg = int(x_coord[0])
    x_end = int(x_coord[1])
    y_end = int(y_coord[0])
    y_beg = int(y_coord[1])
    
Size_x = x_end - x_beg
Size_y = y_end - y_beg

# Part 1

def Calc_max_y(init_y : int):
    max_y = sum(range(init_y))
    return max_y

y_init_max = Calc_max_y(abs(y_end))  
print(y_init_max)

# Part 2
compute_x_min = True
step = 0
x_init_min = 0
while compute_x_min:
    step += 1
    if sum(range(step+1)) > x_beg:
        x_init_min = step
        compute_x_min = False
    
distinct_comb = []
for y_init in range(y_end, -y_end+1):
    y_vel = y_init
    y_dist = y_vel
    while y_dist > y_beg:
        y_vel -= 1
        y_dist += y_vel
    if y_dist >= y_end:
        for x_init in range(x_init_min, x_end+1):
            x_vel = x_init
            x_dist = x_vel
            while x_dist < x_beg and x_vel != 0:
                x_vel -= 1
                x_dist += x_vel
            if x_dist <= x_end:
                distinct_comb.append([x_init, y_init])
                
velocities = []
for vector in distinct_comb:
    velocity = floor(sqrt(vector[0]*vector[0] +vector[1]*vector[1]))
    if velocity not in velocities:
        velocities.append(velocity)
    

print(len(velocities))


from math import sqrt, ceil, floor
from itertools import takewhile, product, chain

x_min = 179
x_max = 201
y_min = -109
y_max = -63

rmin = sqrt(0.25 + 2 * x_min)
rmax = sqrt(0.25 + 2 * x_max)
lower = rmin - 0.5
upper = rmax - 0.5
# all positive ints between lower and upper are valid v_x if t ≥ v_x
joker_v_xs = range(int(ceil(lower)), int(floor(upper)) + 1)

valid_vv = set()

# max number of steps: - y_min * 2
for t in range(1, - y_min * 2 + 1):
    # print(f't = {t}, ', end='')
    # find valid v_y
    v_y_min = y_min / t + t / 2 - 0.5
    v_y_max = y_max / t + t / 2 - 0.5

    valid_v_y = range(int(ceil(v_y_min)), int(floor(v_y_max)) + 1)

    # find valid v_x
    v_x_min = max(x_min / t + t / 2 - 0.5, t)
    v_x_max = x_max / t + t / 2 - 0.5
    valid_v_x = chain(range(int(ceil(v_x_min)), int(floor(v_x_max)) + 1),
                    takewhile(lambda v: v <= t, joker_v_xs))

    valid_vv.update(product(valid_v_x, valid_v_y))


# print(counter)
print(len(valid_vv))