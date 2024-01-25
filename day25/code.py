data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
from collections import defaultdict

# Part 1
# "three bridges"
nodes = defaultdict(set)
for s in data:
    n, nb = s.split(': ')
    for j in nb.split(' '):
        nodes[n].add(j)
        nodes[j].add(n)

left = set(nodes)
count_neighbours = lambda n: len(nodes[n] - left)
while sum(map(count_neighbours, left)) != 3:
    # Remove node with most neighbours in other set
    left.remove(max(left, key=count_neighbours))

print(f'Part 1: {len(left) * (len(nodes) - len(left))}')