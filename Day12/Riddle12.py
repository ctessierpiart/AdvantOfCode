Caves = []
Neighbours = []

from collections import namedtuple

with open('Day12/Caves.csv', 'r') as file:
    for line in file:
        line = line.strip('\n')
        line = line.split('-')
        for index, element in enumerate(line):
            if element not in Caves:
                Caves.append(element)
                Neighbours.append([line[(index+1)%2]])
            else:
                Neighbours[Caves.index(element)].append(line[(index+1)%2])
         
Nodes = {}
for index,node in enumerate(Caves):
    Nodes[node] = {}
    Nodes[node]['Name'] = node
    Nodes[node]['Neighbours'] = Neighbours[index]
    Nodes[node]['Small'] = node.islower()

Total_Paths = []
Path = [[]] 
NUMBER_OF_PATH = 0

def Parcours(Node : str, previous_nodes : list[str]):
    node = Nodes[Node]
    previous_nodes.append(node['Name'])
    if node['Name'] == 'end':
        global NUMBER_OF_PATH
        NUMBER_OF_PATH +=1
    for neighbour in node['Neighbours']:
        if neighbour not in previous_nodes or Nodes[neighbour]['Small'] == False:
            Path.append(previous_nodes)
            Parcours(neighbour, Path[-1])

Parcours('start', Path[0])
print(NUMBER_OF_PATH)