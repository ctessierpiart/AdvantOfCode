##How many measurements are larger than the previous measurement?

Data_Depth = []
with open('Day1/Depth.csv') as file:
    for line in file:
        Depth = int(line)
        Data_Depth.append(Depth) 

previous_depth = Data_Depth[0]
depth_increased = 0
for depth in Data_Depth[1:]:
    if (depth > previous_depth):
        depth_increased += 1
    previous_depth = depth

print(' : '.join(['Part 1 solution', str(depth_increased)]))

depth_increased_glissante = 0
window_with = 3
window_half_width = int((window_with -1)/2)
previous_depth = sum(Data_Depth[0:2*window_half_width+1])
for index, _ in enumerate(Data_Depth[window_half_width:-window_half_width]):
    if (isinstance(Data_Depth[index], int) and isinstance(Data_Depth[index+2*window_half_width], int)):
        depth = sum(Data_Depth[index:index+2*window_half_width+1])
        if (depth > previous_depth):
            depth_increased_glissante += 1
        previous_depth = depth
    
print(' : '.join(['Part 2 solution', str(depth_increased_glissante)]))