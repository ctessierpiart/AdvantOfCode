Numbers = []
Displays = []

with open('Day8/Display.csv', 'r') as file:
    for line in file:
        line = line.strip('\n')
        line = line.split(' | ')
        Numbers.append(line[0].split(' '))
        Displays.append(line[1].split(' '))
        
# Partie 1

count_1478 = 0
for display in Displays:
    for number in display:
        length = len(number)
        match length:
            case 2:
                count_1478 += 1
            case 3:
                count_1478 += 1
            case 4:
                count_1478 += 1
            case 7:
                count_1478 += 1

print(f'Solution 1 : {count_1478}')

# Partie 2
Sum = 0
for index, display in enumerate(Displays):
    number_set= [set('') for _ in range(10)]
    # First pass for easy numbers
    for index_num, string in enumerate(Numbers[index]):
        length = len(string)
        match length:
            case 2:
                number_set[1] = set(string)
            case 3:
                number_set[7] = set(string)
            case 4:
                number_set[4] = set(string)
            case 7:
                number_set[8] = set(string)
    # Deduct other numbers displayed from previous ones
    newDisplay = ''
    for index_num, string in enumerate(display):
        string_set = set(string)
        length = len(string_set)
        match length:
            case 2:
                newDisplay = ''.join([newDisplay, '1'])
            case 3:
                newDisplay = ''.join([newDisplay, '7'])
            case 4:
                newDisplay = ''.join([newDisplay, '4'])
            case 7:
                newDisplay = ''.join([newDisplay, '8'])
            case 5:    #number is 3, 2 or 5
                len_match_with_1 = len(number_set[1] & string_set)
                if len_match_with_1 == 2:
                    newDisplay = ''.join([newDisplay, '3'])
                else:
                    len_match_with_4 = len(number_set[4] & string_set)
                    if len_match_with_4 == 2:
                        newDisplay = ''.join([newDisplay, '2'])
                    else:
                        newDisplay = ''.join([newDisplay, '5'])
            case 6:    #number is 0, 6 or 9
                len_match_with_4 = len(number_set[4] & string_set)
                if len_match_with_4 == 4:
                    newDisplay = ''.join([newDisplay, '9'])
                else:
                    len_match_with_1 = len(number_set[1] & string_set)
                    if len_match_with_1 == 2:
                        newDisplay = ''.join([newDisplay, '0'])
                    else:
                        newDisplay = ''.join([newDisplay, '6'])
    
    Sum += int(newDisplay)
    

print(f'Solution 2 : {Sum}')