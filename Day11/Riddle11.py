import numpy as np

class Squids():
    
    def __init__(self, steps):
        Squids = []
        with open('Day11/Squids.csv', 'r') as file:
            for line in file:
                line = line.strip('\n')
                Squids.append([int(x) for x in line])
        self.Squids = np.array(Squids)
        self.number_flash = 0
        self.steps = steps
        self.current_step = 0

    def Step_Calc(self):
        self.current_step += 1
        self.Squids += 1
        self.new_flash = self.Squids > 9
        self.old_flash = self.Squids < -1
        while sum(sum(self.new_flash)):
            local_flash = np.nditer(self.new_flash, flags=['multi_index'])
            for flash in local_flash:
                if flash == True:
                    y, x = local_flash.multi_index
                    self.Light_emissions(x, y)
            self.old_flash += self.new_flash
            self.new_flash = (self.Squids > 9) ^ self.old_flash
        self.number_flash += sum(sum(self.old_flash))
        if sum(sum(self.old_flash)) == 100:
            print(f'First Step : {self.current_step}')
        self.Squids[self.Squids >9] = 0
            

    def Light_emissions(self, x, y):
        x_begin = x-1
        x_end = x+1
        y_begin = y-1
        y_end = y+1
        if x == 0:
            x_begin = 0
        elif x == 9:
            x_end = 9
        if y == 0:
            y_begin = 0
        elif y == 9:
            y_end = 9
    
        self.Squids[y_begin:y_end+1, x_begin:x_end+1] += 1
        a = 1
        
    def run(self):
        for x in range(self.steps):
            self.Step_Calc()
        print(self.number_flash)
        
if __name__ == '__main__':
       Squids = Squids(1000)
       Squids.run() 