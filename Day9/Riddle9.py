from typing import List
import numpy as np


class Cave():
    
    def __init__(self, path : str):
        Cave = []
        with open(path, 'r') as file:
            for line in file:
                line = line.strip('\n')
                Cave.append([int(x) for x in line])
            
        self.Cave = np.array(Cave)
        (self.X_Size, self.Y_size) = self.Cave.shape
        self.Cave = np.pad(self.Cave, 1, mode = 'constant', constant_values = 10)
        self.Risk = 0
        self.Low_points = []
        self.Bassins = []
        self.Bassin_sizes = []
        self.Bassin_map = self.Cave > 8

    def Single_low_point(self, point):
        y, x = point
        Up =    self.Cave[x, y -1]
        Down =  self.Cave[x, y +1]
        Right = self.Cave[x +1, y]
        Left =  self.Cave[x -1, y]
        Point = self.Cave[x, y]
        if (Point < Up and Point < Down and Point < Right and Point < Left):
            self.Low_points.append((x, y))
            return 1 + Point
        else:
            return 0
            
    def Calc_low_points(self):
        sum_risk = 0
        local_Cave = np.nditer(self.Cave[1:-1, 1:-1], flags=['multi_index'])
        for x in local_Cave:
            y, x = local_Cave.multi_index
            point = (y+1, x+1)
            sum_risk += self.Single_low_point(point)
            
        self.Risk = sum_risk
        
    def Calc_Bassins(self):
        for low_point in self.Low_points:
            bassin = []
            points_to_process = [low_point]
            self.Bassin_map[low_point] = True
            while points_to_process != []:
                bassin = bassin + points_to_process
                points_to_process = self.Adjacent_non_limits(points_to_process, bassin)
            self.Bassins.append(bassin)
            self.Bassin_sizes.append(len(bassin))
                
                
    def Adjacent_non_limits(self, points : list):
        Valid_points = []
        for point in points:
            y, x = point
            Up_point =    (y-1, x)
            Down_point =  (y+1, x)
            Right_point = (y, x+1)
            Left_point =  (y, x-1)
            
            Up =    self.Cave[Up_point]
            Down =  self.Cave[Down_point]
            Right = self.Cave[Right_point]
            Left =  self.Cave[Left_point]
            
            if Up < 9:
                if self.Bassin_map[Up_point] == False:
                    Valid_points.append(Up_point)
                    self.Bassin_map[Up_point] = True
            if Down < 9:
                if self.Bassin_map[Down_point] == False:
                    Valid_points.append(Down_point)
                    self.Bassin_map[Down_point] = True
            if Right < 9:
                if self.Bassin_map[Right_point] == False:
                    Valid_points.append(Right_point)
                    self.Bassin_map[Right_point] = True
            if Left < 9:
                if self.Bassin_map[Left_point] == False:
                    Valid_points.append(Left_point)
                    self.Bassin_map[Left_point] = True
            
        return Valid_points
            
            
if __name__ == '__main__':
    Cave = Cave('Day9/Cave.csv')
    a = 1
    Cave.Calc_low_points()
    print(f'Solution 1 : {Cave.Risk}')
    Cave.Calc_Bassins()
    bassin_sorted_sizes = np.sort(Cave.Bassin_sizes)
    print(f'Solution 2 : {bassin_sorted_sizes[-1]*bassin_sorted_sizes[-2]*bassin_sorted_sizes[-3]}')
    
    