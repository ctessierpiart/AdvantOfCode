import numpy as np

Im_array = []
with open('Day20/Image.txt') as file:
    Enhance_string, Image = file.read().split('\n\n')
    Enhance_string = Enhance_string.strip('\n')
    Enhance_string = [0 if x == '.' else 1 for x in Enhance_string]
    Image = Image.split('\n')
    for line in Image:
        Im_array.append([0 if x == '.' else 1 for x in line])
    Image = np.array(Im_array)