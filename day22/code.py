from collections import defaultdict
from copy import deepcopy
data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()

data.sort(key=lambda s: int(s.split(',')[-1]))

# Part 1
n = 10
ground = [x[:] for x in [[0] * n] * n]
support = [x[:] for x in [['ground'] * n] * n]
resting = defaultdict(set)
unsafe = []

for i, s in enumerate(data):
    c = [[int(m) for m in k.split(',')] for k in s.split('~')]
    x_range = [j for j in range(c[0][0], c[1][0] + 1)]
    y_range = [j for j in range(c[0][1], c[1][1] + 1)]
    height = c[1][2] - c[0][2] + 1
    
    # Find resting place height
    h = 0
    for x in x_range:
        for y in y_range:
            h = max(h, ground[y][x])
    
    # Place
    n_supports = set()
    for x in x_range:
        for y in y_range:
            if ground[y][x] == h:
                n_supports.add(str(support[y][x]))
                resting[support[y][x]].add(str(i))
            ground[y][x] = h + height
            support[y][x] = str(i)
    if len(n_supports) == 1:
        unsafe += list(n_supports)

unsafe = set(unsafe) - {'ground'}
print(f'Part 1: {len(data) - len(unsafe)}')

# Part 2
supporters = defaultdict(set)
for k, v in resting.items():
    for s in v:
        supporters[s].add(k)

total = 0
for d in resting.keys():
    if d == 'ground':
        continue
    d_supporters = deepcopy(supporters)    
    d_supporters[d] = set()

    falls = -1 # only count "additional" removals
    while no_support := [k for k, v in d_supporters.items() if len(v) == 0]:
        falls += 1
        for k in d_supporters.keys():
            d_supporters[k].discard(no_support[0])
        del d_supporters[no_support[0]]
    total += falls

print(f'Part 2: {total}')
