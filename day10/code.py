data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()


def match_pipe(symbol, move):
    match symbol:
        case '|':
            match move:
                case 'down':
                    return 'down'
                case 'up':
                    return 'up'
        case '-':
            match move:
                case 'left':
                    return 'left'
                case 'right':
                    return 'right'
        case 'L':
            match move:
                case 'down':
                    return 'right'
                case 'left': 
                    return 'up'
        case 'J':
            match move:
                case 'down':
                    return 'left'
                case 'right': 
                    return 'up'
        case '7':
            match move:
                case 'up':
                    return 'left'
                case 'right': 
                    return 'down'          
        case 'F':
            match move:
                case 'up':
                    return 'right'
                case 'left': 
                    return 'down'

# Part 1
for i, x in enumerate(data):
    if x.find('S') != -1:
        s = (i, x.find('S'))
        break

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)}

best = 0
for m, d in directions.items():
    pipes = []
    distance = 1
    p = (s[0] + d[0], s[1] + d[1])
    while (p != s) and (0 <= p[0] <= len(data)) and (0 <= p[1] <= len(data[0])):
        pipes.append(p)
        distance += 1
        m = match_pipe(data[p[0]][p[1]], m)
        if m is None:
            distance = 0
            break
        d = directions[m]
        p = (p[0] + d[0], p[1] + d[1])
    if distance > best:
        best = distance
        pipe = [s] + pipes

print(f'Part 1: {best // 2}')
       
# Part 2
inside = []
m = 'up' # Differs per data set, need clockwise rotation from start
d = directions[m]
p = (s[0] + d[0], s[1] + d[1])

moves = {'right': 'down',
         'down': 'left',
         'left': 'up',
         'up': 'right'}
while p != s:
    # Look to the right
    for i in range(1, len(data)):
        l = directions[moves[m]]
        c = (p[0] + l[0] * i, p[1] + l[1] * i)
        if c in pipe:
            break
        inside.append(c)
    # Exception for F left-turns; also look straight
    if data[p[0]][p[1]] == 'F' and m == 'left':
        for i in range(1, len(data)):
            l = d
            c = (p[0] + l[0] * i, p[1] + l[1] * i)
            if c in pipe:
                break
            inside.append(c)
    m = match_pipe(data[p[0]][p[1]], m)
    d = directions[m]
    p = (p[0] + d[0], p[1] + d[1])

print(f'Part 2: {len(set(inside))}')
