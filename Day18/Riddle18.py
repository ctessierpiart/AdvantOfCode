from operator import mod
from math import floor
import copy

SnailNumbersList = []

with open('Day18/Snailnumbers.txt') as file:
    for line in file:
        line = line.strip('\n')
        SnailNumbersList.append(line)


def flatinput(input):
    flatlist = []
    for number in input:
        flatlist.append(flatNumber(number))
    return flatlist

def flatNumber(Number):
    flatline = []
    depth = 0
    for char in Number:
        if char == '[':       
            depth += 1
        elif char == ']':     
            depth -= 1
        elif char.isdigit():  
            flatline.append([int(char), depth])
    return flatline

def SnailAdd(NumberA, NumberB):
    NewNumber = NumberA + NumberB
    for Number in NewNumber:
        Number[1] += 1
    return NewNumber
        
def SnailReduce(Number):
    SnailNumber = copy.deepcopy(Number)
    Checked = True
    while (Checked):
        Checked = False
        Exploded = False
        ##Explode
        for indexNumber, Number in enumerate(SnailNumber):
            if Number[1] > 4:
                Checked = True
                Exploded = True
                if indexNumber == 0:
                    SnailNumber[2][0] += SnailNumber[1][0]
                elif indexNumber == len(SnailNumber) - 2:
                    SnailNumber[indexNumber-1][0] += Number[0]
                else:
                    SnailNumber[indexNumber-1][0] += Number[0]
                    SnailNumber[indexNumber+2][0] += SnailNumber[indexNumber+1][0]
                depth = Number[1]
                del SnailNumber[indexNumber:indexNumber+2]
                SnailNumber.insert(indexNumber, [0, depth-1])
                
                break
        ##Split
        if Exploded is False:
            for indexNumber, Number in enumerate(SnailNumber):
                if Number[0] > 9:
                    Checked = True
                    LeftNumber = floor(Number[0]/2)
                    RightNumber = Number[0] - LeftNumber
                    depth = Number[1] + 1
                    
                    del SnailNumber[indexNumber]
                    SnailNumber.insert(indexNumber, [RightNumber, depth])
                    SnailNumber.insert(indexNumber, [LeftNumber, depth])
                    break
                 
    return SnailNumber

def CheckMagnitude(SnailNumber):
    MagnitudeNumber = copy.deepcopy(SnailNumber)
    depth = 4
    while depth != 0:
        for indexNumber, number in enumerate(MagnitudeNumber):
            if number[1] == depth:
                if (MagnitudeNumber[indexNumber][1] == depth):
                    Value = number[0]*3 + MagnitudeNumber[indexNumber+1][0]*2
                    del MagnitudeNumber[indexNumber]
                    del MagnitudeNumber[indexNumber]
                    MagnitudeNumber.insert(indexNumber, [Value, depth-1])
                else:
                    
        depth -= 1
    return MagnitudeNumber[0][0]
    

FlatInput = flatinput(SnailNumbersList)
ReducedNumber = copy.deepcopy(FlatInput[0])
for input in FlatInput[1:]:
    TempNumber = SnailAdd(ReducedNumber, input)
    ReducedNumber = SnailReduce(TempNumber)
Magnitude = CheckMagnitude(ReducedNumber)
print(Magnitude)

maxMagnitude = 0
for indexInput, input in enumerate(FlatInput):
    for secondinput in FlatInput[indexInput+1:]:
        Magnitude = CheckMagnitude(SnailReduce(SnailAdd(input, secondinput)))
        if Magnitude > maxMagnitude:
            maxMagnitude = Magnitude