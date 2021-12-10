from collections import namedtuple
import numpy as np

CommandLines = []

with open('Day10/Input.csv', 'r') as file:
    for line in file:
        line = line.strip('\n')
        CommandLines.append(line)
        
Openning_statement = ['(', '[', '{', '<']
Closing_statement = [')', ']', '}', '>']
Score_points = [3, 57, 1197, 25137]

Score = 0
uncorrupted_statement = []
for line in CommandLines:
    new_line = line
    while True:
        len_before = len(new_line)
        new_line = new_line.replace('()', '')
        new_line = new_line.replace('{}', '')
        new_line = new_line.replace('[]', '')
        new_line = new_line.replace('<>', '')
        len_after = len(new_line)
        if len_before == len_after:
            break
        
    is_corrupted = False
    for index, char in enumerate(new_line):
        if char in Closing_statement:
            match char:
                case ')':
                    char_score = 3
                case ']':
                    char_score = 57
                case '}':
                    char_score = 1197
                case '>':
                    char_score = 25137
            Score += char_score
            is_corrupted = True
            break
    
    if is_corrupted == False:
        uncorrupted_statement.append(new_line)

print(f'Solution 1 : {Score}')

Scores = []
for line in uncorrupted_statement:
    Score = 0
    for char in reversed(line):
        Score *= 5
        match char:
            case '(':
                Score += 1
            case '[':
                Score += 2
            case '{':
                Score += 3
            case '<':
                Score += 4
    Scores.append(Score)
    
Solution = np.median(Scores)
Solution = int(Solution)

print(f'Solution 2 : {Solution}')