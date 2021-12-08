Numbers = []
Displays = []

with open('Day8/Display.csv', 'r') as file:
    for line in file:
        line = line.strip('\n')
        line = line.split(' | ')
        Numbers.append(line[0].split(' '))
        Displays.append(line[1].split(' '))
        
# Partie 1
number_length = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

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
for index, display in enumerate(Displays):
    number_string = ['' for _ in range(10)]
    # First pass for easy numbers
    for index_num, string in enumerate(Numbers[index]):
        length = len(string)
        match length:
            case 2:
                number_string[1] = string
            case 3:
                number_string[7] = string
            case 4:
                number_string[4] = string
            case 7:
                number_string[8] = string
    # Deduct other numbers from previous ones
    for index_num, string in enumerate(Numbers[index]):
        length = len(string)
        match length:
            case 5:
                
                
                if (number_string[1] in string):
                    number_string[3] = string
                else:
                    num4_7 = set(''.join([number_string[4], number_string[7]]))
                    set_string = set(string)
                    length = len(num4_7 & set_string)
                    if length == 3:
                        number_string[2] = string
                    else:
                        number_string[5] = string
            case 6:
                
