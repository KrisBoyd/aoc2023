import sys
sys.setrecursionlimit(10_000)
from collections import defaultdict

data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()

# Part 1
PART = 1
start = (0, 1)
visited = [(0, 1)]
def find_paths(data, visited, p, length=1):
    moves = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}
    for m, d in moves.items():
        p_n = (p[0] + d[0], p[1] + d[1])
        if p_n == (len(data) - 1, len(data[0]) - 2):
            yield length

        elif (0 <= p_n[0] <= (len(data) - 1)) and (0 <= p_n[0] <= (len(data[0]) - 1)):
            if p_n not in visited:
                loc = data[p_n[0]][p_n[1]]
                if (loc == '.') or \
                   (loc == '^' and m == 'up') or \
                   (loc == '>' and m == 'right') or \
                   (loc == 'v' and m == 'down') or \
                   (loc == '<' and m == 'left'):
                    for path in find_paths(data, visited + [p_n], p_n, length + 1):
                        yield path

print(f'Part 1: {max([p for p in find_paths(data, visited, p=start)])}')

# Part 2
nodes = defaultdict(set)
visited = [(0, 1)]
def connect_nodes(data, node, p, length):
    global nodes
    global visited
    moves = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}
    next = [(p[0] + d[0], p[1] + d[1]) for d in moves.values()]
    next = [n for n in next if 0 <= n[0] <= (len(data) - 1) and 0 <= n[1] <= (len(data[0]) - 1)]
    next = [n for n in next if data[n[0]][n[1]] != '#']
    next = list(set(next) - (set(visited) - set(nodes)) - {node})

    if p == (len(data)- 1, len(data) - 2): # reach the end
        nodes[node].add((p, length))
    if len(next) >= 2 or p in nodes: # found a node
        nodes[node].add((p, length))
        nodes[p].add((node, length))
        for n in next:
            visited += [n]
            connect_nodes(data, p, n, 1)
    elif len(next) == 1:
        visited += [next[0]]
        connect_nodes(data, node, next[0], length + 1)

connect_nodes(data, node=(0, 1), p=(0, 1), length=0)

def find_node_paths(nodes, vis, p, length=1):
    for node in nodes[p]:
        if node[0] == (len(data) - 1, len(data[0]) - 2):
            yield length + node[1]
        if node[0] in vis:
            continue
        for path in find_node_paths(nodes, vis + [node[0]], node[0], length + node[1]):
            yield path

print(f'Part 2: {max([c for c in find_node_paths(nodes, vis=[(0, 1)], p=(0, 1), length=0)])}')
