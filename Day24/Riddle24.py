from operator import mod
from math import floor

operation_list = []

with open('Day24/MONAD.txt') as file:
    for line in file:
        line = line.strip('\n')
        operation = line.split(' ')
        operation_list.append(operation)
        
operation_list_by_digit  = []
index = 0
for digit in range(14):
    digit_spec = []
    digit_spec.append(operation_list[index])
    index += 1
    for operation in operation_list[index:]:
        if (operation != digit_spec[0]):
            digit_spec.append(operation)
            index += 1
        else:
            break
    operation_list_by_digit.append(digit_spec)
        
def decode_ALU(operation, data=0):
    op_type = operation[0]
    if (len(operation) == 2):
        a = data
    else:
        a = operation[1]
        b = operation[2]
        match(op_type):
            case('add'):
                a += b
            case('mul'):
                a *= b
            case('div'):
                a = floor(a/b)
            case('mod'):
                a = mod(a,b)
            case('eql'):
                a = (a == b)
    return a
        
class ALUmem():
    def __init__(self):
        self.wValue = 0
        self.xValue = 0
        self.yValue = 0
        self.zValue = 0
        
    def read(self, name):
        match(name):
            case('w'):
                return self.wValue
            case('x'):
                return self.xValue
            case('y'):
                return self.yValue
            case('z'):
                return self.zValue
    
    def write(self, name, data):
        match(name):
            case('w'):
                self.wValue = data
            case('x'):
                self.xValue = data
            case('y'):
                self.yValue = data
            case('z'):
                self.zValue = data
    
    def decode(self, operation, data=0):
        op_type = operation[0]
        a = operation[1]
        if (len(operation) == 2):
            self.write(a, data)
        else:
            b = operation[2]
            aValue = self.read(a)
            if (b > 'a' and b <= 'z'):
                bValue = self.read(b)
            else:
                bValue = int(b)
                
            match(op_type):
                case('add'):
                    self.write(a, aValue + bValue)
                case('mul'):
                    self.write(a, aValue * bValue)
                case('div'):
                    self.write(a, floor(aValue/bValue))
                case('mod'):
                    self.write(a, mod(aValue, bValue))
                case('eql'):
                    self.write(a, int(aValue == bValue))
        a = 0
        
    def reset(self):
        self.wValue = 0
        self.xValue = 0
        self.yValue = 0
        self.zValue = 0
    
ALU = ALUmem()

        
def test_serial(serial_number : int):
    for digit_index, digit in enumerate(serial_number):
        for operation_index, operation in enumerate(operation_list_by_digit[digit_index]):
            if (operation_index == 0):
                ALU.decode(operation, int(serial_number[digit_index]))
            else:
                ALU.decode(operation)
    result = ALU.read('z')
    ALU.reset()
    return result

serial_test = '13579246899999'
print(test_serial(serial_test))

def bruteForce():
    validSerial = []
    for serialNumber in range (11111111111111, 99999999999999 + 1):
        okString = True
        serialString = format(serialNumber, '014d')
        for char in serialString:
            if char == '0':
                okString = False
                break;
        if (okString):
            if(test_serial(serialString) == 0):
                validSerial.append(serialString)
                
    return validSerial