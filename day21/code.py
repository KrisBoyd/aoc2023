from copy import deepcopy
data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()

for i, x in enumerate(data):
    if 'S' in x:
        p = (i, x.find('S'))
        break
    

# Part 1
gardens = {}
for i, x in enumerate(data):
    for j, y in enumerate(x):
        if y == 'S':
            p = (i, j)
            gardens[p] = 0
        elif y == '.':
            gardens[(i, j)] = 1000

def neighbours(p, gardens):
    nb = [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]
    nb = [s for s in nb if s in gardens]
    return nb


solved = [p]
nodes = [p]

while len(nodes):
    new_nodes = []
    for n in nodes:
        nbs = neighbours(n, gardens)
        nbs = [s for s in nbs if gardens[s] == 1000]
        for nb in nbs:
            gardens[nb] = gardens[n] + 1
        new_nodes += nbs
    nodes = new_nodes

steps = 64
r = len([v for v in gardens.values() if v <= steps and v % 2 == 0])
print(f'Part 1: {r}')
       
# Part 2
steps = 26501365
k = (steps - 65) / 131

r = len([v for v in gardens.values() if v != 1000 and v % 2 == 1]) # value within area
areas = (k*2+1)**2 - 4 * (k*(k+1)) / 2 # square minus triangular corners
diamond = len([v for v in gardens.values() if v <= len(data) and v % 2 == 1])
res = (areas - 1) * r + diamond + k*117+k**2
print(f'Part 2: {res}')
