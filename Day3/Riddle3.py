Gamma_Rate = 0         #Most common bit
Epsilon_Rate = 0       #Least common bit

Binaries = []
with open('Day3/BinaryInput.csv') as file:
    for line in file:
        line = line.strip()
        Binaries.append([char for char in line] )


for index, value in enumerate(Binaries[0]):
    On_bit = 0
    for power in Binaries:
        if power[index] == "1":
            On_bit += 1
        else:
            On_bit -= 1
    if On_bit > 0:
        Gamma_Rate += 1 * 2**(len(Binaries[0]) - index - 1)
    else:
        Epsilon_Rate += 1 * 2**(len(Binaries[0]) - index - 1)
        
print(''.join(['Gamma_Rate = ', str(Gamma_Rate)]))
print(''.join(['Binary representation : ', '{0:012b}'.format(Gamma_Rate)]))

print(''.join(['Epsilon_Rate = ', str(Epsilon_Rate)]))
print(''.join(['Binary representation : ', '{0:012b}'.format(Epsilon_Rate)]))

print(f'Solution 1 is {Gamma_Rate*Epsilon_Rate}')

valid_indexes = [1 for n in Binaries]
#Oxygen generation
Oxy_gen = 0
is_over = False
for index, value in enumerate(Binaries[0]):
    On_bit = 0
    for index_crit, power in enumerate(Binaries):
        if valid_indexes[index_crit] == 1:
            if power[index] == "1":
                On_bit += 1
            else:
                On_bit -= 1
                
    if On_bit >= 0:
        Criteria = "1"
    else:
        Criteria = "0"
        
    for index_crit, power in enumerate(Binaries):
        if power[index] != Criteria:
            valid_indexes[index_crit] = 0
            
    if sum(valid_indexes) == 1:
        valid_index = valid_indexes.index(1)
        Oxy_gen = int(Binaries[valid_index], 2)
        is_over = True
    
    if is_over == True:
        break
    
print(f'Oxygen generation report : {Oxy_gen}')

valid_indexes = [1 for n in Binaries]
#Oxygen generation
C0_scrub = 0
is_over = False
for index, value in enumerate(Binaries[0]):
    On_bit = 0
    for index_crit, power in enumerate(Binaries):
        if valid_indexes[index_crit] == 1:
            if power[index] == "1":
                On_bit += 1
            else:
                On_bit -= 1
                
    if On_bit >= 0:
        Criteria = "0"
    else:
        Criteria = "1"
        
    for index_crit, power in enumerate(Binaries):
        if power[index] != Criteria:
            valid_indexes[index_crit] = 0
            
    if sum(valid_indexes) == 1:
        valid_index = valid_indexes.index(1)
        C0_scrub = int(Binaries[valid_index], 2)
        is_over = True
    
    if is_over == True:
        break
    
print(f'C02 scrubbing report : {C0_scrub}')

print(f'Solution 2 is {C0_scrub*Oxy_gen}')