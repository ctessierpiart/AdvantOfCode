from collections import Counter, defaultdict
Rules = {}

with open('Day14/Chain.csv', 'r') as file:
    first_chain, swap_rules = file.read().split('\n\n')
    swap_rules = swap_rules.split('\n')
    for rule in swap_rules:
        Base_pair, swap = rule.split(' -> ')
        Swap1 = ''.join([Base_pair[0], swap])
        Swap2 = ''.join([swap, Base_pair[1]])
        Ref = swap
        Rules[Base_pair] = [Swap1, Swap2, swap]

first_pairs = [first_chain[index:index+2] for index, char in enumerate(first_chain[:-1])]
Occurences = Counter(first_pairs)
for key, value in Rules.items():
    if key not in Occurences:
        Occurences[key] = 0

Char_occurence = Counter(first_chain)

Nbstep = 40
for step in range(Nbstep):
    new_occurences = Counter()
    for pair in Occurences:
        new_occurences[Rules[pair][0]] += Occurences[pair]
        new_occurences[Rules[pair][1]] += Occurences[pair]
        Char_occurence[Rules[pair][2]] += Occurences[pair]
    Occurences = new_occurences

most_common_char, nb_most_common = Char_occurence.most_common()[0]

least_common_char, nb_least_common = Char_occurence.most_common()[-1]

print(f'Solution 1 = {nb_most_common - nb_least_common}')