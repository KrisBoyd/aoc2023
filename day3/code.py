from collections import defaultdict
data = open("day3/data.txt", "r").read().splitlines()

def find_neighbours(a, b, data, idx = False):
    range_i = set([max(0, a - 1), a, min(len(data) - 1, a + 1)])
    range_j = set([max(0, b - 1), b, min(len(data) - 1, b + 1)])
    neighbours = []
    for i in range_i:
        for j in range_j:
            if not (i == a and j == b):
                if idx:
                    neighbours += [((i, j), data[i][j])]
                else:
                    neighbours += [data[i][j]]
    return neighbours

# Part 1
res = 0
num = ''
neighbours = []
for i, x in enumerate(data):
    for j, y in enumerate(x):
        if y in '0123456789':
            num += y
            neighbours += find_neighbours(i, j, data)
        else:
            if len(num):   
                if len(set(neighbours) - set('0123456789') - {'.'}):
                    res += int(num)
                num = ''
                neighbours = []

print(f'Part 1: {res}')
         
# Part 2
gears = defaultdict(list)
num = ''
neighbours = []
for i, x in enumerate(data):
    for j, y in enumerate(x):
        if y in '0123456789':
            num += y
            neighbours += find_neighbours(i, j, data, idx=True)
        else:
            if len(num):
                adjacent_gears = [s[0] for s in neighbours if s[1] == '*']
                for g in set(adjacent_gears):
                    gears[g] += [int(num)]
                neighbours = []
                num = ''

print('Part 2:')
print(sum([s[0] * s[1] for s in gears.values() if len(s) == 2]))
