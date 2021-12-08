X_pos = 0
Y_pos = 0

with open('Day2/Commands.csv') as file:
    for line in file:
        command, value = line.split(' ')
        value = int(value)
        full_command = (command, value)
        match full_command:
            case ('forward', _):
                X_pos += value
            case ('down', _):
                Y_pos += value
            case ('up', _):
                Y_pos -= value
                
XY = X_pos * Y_pos

print(''.join(['Position finale : X = ', str(X_pos)]))
print(''.join(['Profondeur finale : Y = ', str(Y_pos)]))
print(''.join(['Solution 1 : XY = ', str(XY)]))

X_pos = 0
Y_pos = 0
aim = 0

with open('Day2/Commands.csv') as file:
    for line in file:
        command, value = line.split(' ')
        value = int(value)
        full_command = (command, value)
        match full_command:
            case ('forward', _):
                X_pos += value
                Y_pos += value*aim
            case ('down', _):
                aim += value
            case ('up', _):
                aim -= value
                
XY = X_pos * Y_pos

print(''.join(['Position finale : X = ', str(X_pos)]))
print(''.join(['Profondeur finale : Y = ', str(Y_pos)]))
print(''.join(['Solution 2 : XY = ', str(XY)]))
        