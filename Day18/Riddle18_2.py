from typing import NewType

SnailNumbersList = []

with open('Day18/Snailnumbers.txt') as file:
    for line in file:
        line = line.strip('\n')
        SnailNumbersList.append(line)
        
class Snailnumber:
    def __init__(self, parent, rightNumber, leftNumber, value):
        self.parent = parent             ##Parent Number
        self.rightNumber = rightNumber   ##Right member
        self.leftNumber = leftNumber     ##Left member
        self.value = value               ##Value of a single digit inside a number
        
Snailnumber_class = NewType('Snailnumber_class', Snailnumber)
        
def String2Tree(stringNumber : str):
    ##If only a digit
    if stringNumber[0] != '[':
        return Snailnumber(None, None, None, int(stringNumber[0]))
    
    depth = 0
    for index, char in enumerate(stringNumber[1:]):
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
            
        if depth == 0:
            return Snailnumber(None, String2Tree(stringNumber[1:index+2]), String2Tree(stringNumber[index+3:-1]), None)
        ##We don't know the parent yet
        
def searchParent(Snailnumber : Snailnumber_class): #define parents
    while Snailnumber.rightNumber != None and Snailnumber.rightNumber.parent == None:
        Snailnumber.rightNumber.parent = Snailnumber
        searchParent(Snailnumber.rightNumber)
    while Snailnumber.leftNumber != None and Snailnumber.leftNumber.parent == None:
        Snailnumber.leftNumber.parent = Snailnumber
        searchParent(Snailnumber.leftNumber)
        
Test = String2Tree(SnailNumbersList[0])
searchParent(Test)
a = 0