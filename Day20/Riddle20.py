import numpy as np
import matplotlib.pyplot as plt

Im_array = []
with open('Day20/Image.txt') as file:
    Enhancer_string, Image = file.read().split('\n\n')
    Enhancer_string = Enhancer_string.strip('\n')
    Enhancer = [0 if x == '.' else 1 for x in Enhancer_string]
    Image = Image.split('\n')
    for line in Image:
        Im_array.append([0 if x == '.' else 1 for x in line])
    Image = np.array(Im_array)

def Image_enhancement(Image, nb_enhance):
    offset = nb_enhance*2
    Image_padded =  np.pad(Image, offset, mode='constant', constant_values = 0)
    for step in range(nb_enhance):
        Image_copy = np.copy(Image_padded)
        Size_y, Size_x = Image_padded.shape
        for y_coord in range(1, Size_y-1):
            for x_coord in range(1, Size_x-1):
                upper =  Image_padded[y_coord-1 ,x_coord -1 : x_coord +2]
                middle = Image_padded[y_coord   ,x_coord -1 : x_coord +2]
                lower =  Image_padded[y_coord+1 ,x_coord -1 : x_coord +2]
                enhance_string = ''.join([str(x) for x in upper]+[str(y) for y in middle]+[str(z) for z in lower])
                enhance_int = int(enhance_string, 2)
                Image_copy[y_coord, x_coord] = Enhancer[enhance_int]
        Image_padded = Image_copy
        print(f'step {step}')
    return Image_padded[nb_enhance:-nb_enhance, nb_enhance:-nb_enhance]

# Part 1

Image_redim = Image_enhancement(Image, 2)
plt.imshow(Image_redim)
plt.show()
    
print(f'Solution 1 : {sum(sum(Image_redim))}')

# Part 2

Image_redim = Image_enhancement(Image, 50)

plt.imshow(Image_redim)
plt.show()
print(f'Solution 2 : {sum(sum(Image_redim))}')
    