import numpy as np

x_pos = 0
y_pos = 1

Begin_points = []
End_points = []
with open('Day5/Lines.csv', 'r') as file:
    for line in file:
        line = line.strip('\n')
        line = line.split(' -> ')
        Begin_strings = line[0].split(',')
        End_strings = line[1].split(',')
        Begin_points.append([int(x) for x in Begin_strings])
        End_points.append([int(x) for x in End_strings])

Map_size = [1000, 1000]
Map = np.zeros(Map_size).astype(int)

def check_no_diag(Begin_point: list[int], End_point: list[int]):
    status = 'is_diag'
    if Begin_point[x_pos] - End_point[x_pos] == 0:
        status = 'is_vert'
    elif Begin_point[y_pos] - End_point[y_pos] == 0:
        status = 'is_hori'
    return status

def draw_line(Begin_point: list[int], End_point: list[int], status: int):
    match status:
        case 'is_hori':
            if Begin_point[x_pos] < End_point[x_pos]:
                Map[Begin_point[x_pos]:End_point[x_pos]+1, Begin_point[y_pos]] +=1
            else:
                Map[End_point[x_pos]:Begin_point[x_pos]+1, Begin_point[y_pos]] +=1
        case 'is_vert':
            if Begin_point[y_pos] < End_point[y_pos]:
                Map[Begin_point[x_pos], Begin_point[y_pos]:End_point[y_pos]+1] +=1
            else:
                Map[Begin_point[x_pos], End_point[y_pos]:Begin_point[y_pos]+1] +=1
        case 'is_diag':
            state_diag = (Begin_point[x_pos] < End_point[x_pos], Begin_point[y_pos] < End_point[y_pos])
            match state_diag:
                case (True, True):
                    for p in range(End_point[x_pos] - Begin_point[x_pos] + 1):
                        Map[Begin_point[x_pos] + p, Begin_point[y_pos] + p] += 1
                case (True, False):
                    for p in range(End_point[x_pos] - Begin_point[x_pos] + 1):
                        Map[Begin_point[x_pos] + p, Begin_point[y_pos] - p] += 1
                case (False, True):
                    for p in range(Begin_point[x_pos] - End_point[x_pos] + 1):
                        Map[Begin_point[x_pos] - p, Begin_point[y_pos] + p] += 1
                case (False, False):
                    for p in range(Begin_point[x_pos] - End_point[x_pos] + 1):
                        Map[Begin_point[x_pos] - p, Begin_point[y_pos] - p] += 1

    
for index, begin_point in enumerate(Begin_points):
    end_point = End_points[index]
    status = check_no_diag(begin_point, end_point)
    draw_line(begin_point, end_point, status)

Map_overlap = Map > 1
Solution = sum(sum(Map_overlap))

print(Solution)
