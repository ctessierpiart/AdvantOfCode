from collections import Counter
Rules = {}

with open('Day14/Chain.csv', 'r') as file:
    first_chain, swap_rules = file.read().split('\n\n')
    swap_rules = swap_rules.split('\n')
    for rule in swap_rules:
        Base_pair, swap = rule.split(' -> ')
        Swap1 = ''.join([Base_pair[0], swap])
        Swap2 = ''.join([swap, Base_pair[1]])
        Rules[Base_pair] = [Swap1, Swap2]


Pair_counter =  []
first_pairs = [first_chain[index:index+2] for index, char in enumerate(first_chain[:-1])]
first_occurences = Counter(first_pairs)
for key, value in Rules.items():
    counter = 0
    if key in first_occurences:
        counter = first_occurences[key]
    Pair_counter.append(counter)
Pair_list = list(Rules)

Nbstep = 100
for step in range(Nbstep-1):
    for pair in Pair_counter:
        if pair != 0:
            Pair_counter[Rules]