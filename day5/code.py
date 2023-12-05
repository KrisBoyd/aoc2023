from collections import defaultdict
data = open("day5/data.txt", "r").read().splitlines()
data = [s for s in data if s != '']
seeds = [int(s) for s in data[0].split(': ')[1].split(' ')]

map = defaultdict(list) 
i = 0
for s in data[2:]:
    if not s[0].isdigit():
        i += 1
    else:
        map[i] += [[int(d) for d in s.split(' ')]]

# Part 1
locations = []
for s in seeds:
    for m in range(len(map)):
        for l in map[m]:
            if s >= l[1] and s < (l[1] + l[2]):
                s += (l[0] - l[1])
                break
    locations += [s]


print(f'Part 1: {min(locations)}')
       
# Part 2
seeds = list(zip(seeds[0::2], seeds[1::2]))

# fill gaps in map[m]
for m in range(len(map)):
    map[m].sort(key = lambda x: x[1])
    if map[m][0][1] != 0:
        map[m] = [[0, 0, map[m][0][1]]] + map[m]
    map[m] = map[m] + [[map[m][-1][1] + map[m][-1][2], 
                        map[m][-1][1] + map[m][-1][2], 1e10]]
    for i in range(len(map[m]) - 1):
        if map[m][i][1] + map[m][i][2] != map[m][i+1][1]:
            map[m] += [[map[m][i][1] + map[m][i][2], 
                        map[m][i][1] + map[m][i][2], 
                        map[m][i+1][1] - (map[m][i][1] + map[m][i][2])]]

for m in range(len(map)):
    new_seeds = []
    for seed_start, seed_range in seeds:
        seed_end = seed_start + seed_range - 1
        for l in map[m]:
            if l[1] <= seed_end and (l[1] + l[2] - 1) >= seed_start:
                if l[1] >= seed_start:
                    right = min(l[1] + l[2] - 1, seed_end)
                    left = l[1]
                    new_seeds += [(left + (l[0] - l[1]), right - left + 1)]
                else:
                    right = min(l[1] + l[2] - 1, seed_end)
                    left = seed_start
                    new_seeds += [(left + (l[0] - l[1]), right - left + 1)]
     
    seeds = new_seeds

print(f'Part 2: {min([s[0] for s in seeds])}')
