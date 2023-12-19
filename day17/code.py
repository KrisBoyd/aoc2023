data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
from collections import defaultdict

# Part 1
moves = {'right': (0, 1),
         'left': (0, -1),
         'up': (-1, 0),
         'down': (1, 0)}
reverser = {'right': 'left', 'up': 'down', 'down': 'up', 'left': 'right'}
heat = {m: defaultdict() for m in moves}
res = []
best = min(982, (len(data[0]) + len(data[1])) * 9)
p = (0, 0)
def path_finder(data, moves, paths):
    global res
    global heat
    global best

    next_paths = []
    for path in paths:
        p = path[0][-1]
        history = path[1]
        score = path[3]
        if p == (len(data) - 1, len(data[0]) - 1):
            # reached the target
            best = min(best, score)
            res = path[0]
            continue
        if score + (len(data) - 1 - p[0]) + (len(data[0]) -1 - p[1]) >= best:
            continue
        for k, m in moves.items():
            if len(history) >= 1 and k == reverser[history[-1]]:
                continue
            if len(history) >= 3 and (history[-1] == history[-2] == history[-3] == k):
                continue
            p_n = (p[0] + m[0], p[1] + m[1])
            if p_n not in path[0]:
                if (0 <= p_n[0] < len(data)) and (0 <= p_n[1] < len(data[0])):
                    hist = k
                    if len(history) >= 1 and history[-1] == k:
                        hist += k
                        if len(history) >= 2 and history[-2] == k:
                            hist += k
                    if hist not in heat:
                        heat[hist] = {}
                    if p_n not in heat[hist]:
                        heat[hist][p_n] = score
                    elif score <= heat[hist][p_n]:
                        heat[hist][p_n] = score
                    else:
                        continue
                    next_paths += [[path[0] + [p_n], 
                                    history[-2:] + [k],
                                    hist,
                                    score + int(data[p_n[0]][p_n[1]])]]
    if len(next_paths):
        # filter more
        next_paths = [p for p in next_paths if heat[p[2]][p[0][-1]] == (p[-1] - int(data[p[0][-1][0]][p[0][-1][1]]))]
        pos = []
        filter_paths = []
        for p in next_paths:
            if (p[0][-1], p[2]) not in pos:
                pos += [(p[0][-1], p[2])]
                filter_paths += [p]
        next_paths = filter_paths

        print(f'{len(next_paths)} - {next_paths[0][-1]}')
        return path_finder(data, moves, next_paths)

# path_finder(data, moves, paths = [[[(0, 0)], [], '', 0]])

print(f'Part 1: {best}')

tmp = [''] * len(data)
for i in range(len(data)):
    for j in range(len(data[0])):
        if (i, j) in res:
            tmp[i] += '#'
        else:
            tmp[i] += data[i][j]
[print(t) for t in tmp]

# Part 2
heat = {m: defaultdict() for m in moves}
res = []
best = (len(data[0]) + len(data[1])) * 5
p = (0, 0)
def path_finder(data, moves, paths):
    global res
    global heat
    global best

    next_paths = []
    for path in paths:
        p = path[0][-1]
        history = path[1]
        score = path[3]
        if p == (len(data) - 1, len(data[0]) - 1):
            # reached the target
            if len(set(history[-4:])) > 1: # part 2
                continue
            else:
                print(best)
                best = min(best, score)
                res = path[0]
                continue
        if score + (len(data) - 1 - p[0]) + (len(data[0]) -1 - p[1]) >= best:
            continue
        
        possible_moves = moves
        if len(history):
            # Part 1
            # if len(set(history[-3:])) == 1:
            #     possible_moves = {k: v for k, v in moves.items() if k != history[-1]}

            # Part 2
            if len(history) < 4 or (len(set(history[-4:])) > 1):
                possible_moves = {k: v for k, v in moves.items() if k == history[-1]}
            elif len(history) >= 10 and len(set(history[-10:])) == 1:
                possible_moves = {k: v for k, v in moves.items() if k != history[-1]}
        for k, m in possible_moves.items():
            if len(history) >= 1 and k == reverser[history[-1]]:
                continue
            p_n = (p[0] + m[0], p[1] + m[1])
            if p_n not in path[0]:
                if (0 <= p_n[0] < len(data)) and (0 <= p_n[1] < len(data[0])):
                    hist = path[2]
                    if hist == '' or hist.split(',')[-1] != k:
                        hist = k
                    else:
                        hist = hist + ',' + k
                    
                    if hist not in heat:
                        heat[hist] = {}
                    if p_n not in heat[hist]:
                        heat[hist][p_n] = score
                    elif score <= heat[hist][p_n]:
                        heat[hist][p_n] = score
                    else:
                        continue
                    next_paths += [[path[0] + [p_n], 
                                    history + [k],
                                    hist,
                                    score + int(data[p_n[0]][p_n[1]])]]
    if len(next_paths):
        # filter more
        next_paths = [p for p in next_paths if heat[p[2]][p[0][-1]] == (p[-1] - int(data[p[0][-1][0]][p[0][-1][1]]))]
        pos = []
        filter_paths = []
        for p in next_paths:
            if (p[0][-1], p[2]) not in pos:
                pos += [(p[0][-1], p[2])]
                filter_paths += [p]
        next_paths = filter_paths

        print(f'{len(next_paths)} - {next_paths[0][-1]} - {next_paths[0][0][-1]}')
        return path_finder(data, moves, next_paths)

path_finder(data, moves, paths = [[[(0, 0)], [], '', 0]])

print(f'Part 2: {best}')

tmp = [''] * len(data)
for i in range(len(data)):
    for j in range(len(data[0])):
        if (i, j) in res:
            tmp[i] += '#'
        else:
            tmp[i] += data[i][j]
[print(t) for t in tmp]
