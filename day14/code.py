data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()

def transform_list(l, flip=False):
    n, m = len(l), len(l[0])
    t = []
    for j in range(m):
        t.append('')
        for i in range(n):
            t[j] += l[i][j]
    if flip:
        t = [s[::-1] for s in t]

    return t

# Part 1
rocks = transform_list(data, flip=False)
total = 0
for c in rocks:
    v = len(c)
    for i, x in enumerate(c):
        if x == 'O':
            total += v
            v -= 1
        elif x == '#':
            v = len(c) - i - 1

print(f'Part 1: {total}')

# Part 2
def move_rocks(rocks):
    next_rocks = []
    for r, row in enumerate(rocks):
        next_rocks.append('')
        for i, x in enumerate(row):
            if x == 'O':
                next_rocks[r] += 'O'
            if x == '#':
                next_rocks[r] += '.' * (i - len(next_rocks[r])) + '#'
        if len(next_rocks[r]) != len(row):
            next_rocks[r] += '.' * (i - len(next_rocks[r])) + '.'
    return next_rocks

# rotate
scores = []
rocks = data.copy()
for K in range(1000):
    cycle = ('n', 'w', 's', 'e')
    for c in cycle:
        if c == 'n':
            rocks = transform_list(rocks)
        if c == 'w':
            pass
        if c == 's':
            rocks = transform_list(rocks)
            rocks = [r[::-1] for r in rocks]
        if c == 'e':
            rocks = [r[::-1] for r in rocks]
        
        rocks = move_rocks(rocks)

        if c == 'n':
            rocks = transform_list(rocks)
        if c == 'w':
            pass
        if c == 's':
            rocks = [r[::-1] for r in rocks]
            rocks = transform_list(rocks)
        if c == 'e':
            rocks = [r[::-1] for r in rocks]  
    # print(f'\n\n -- {K} --')        
    # [print(r) for r in rocks]
    scores += [sum([r.count('O') * (i+1) for i, r in enumerate(reversed(rocks))])]

# Find pattern
stable = scores[-100:]
for i in range(3, 100):
    if stable[:i] == stable[i:i*2] == stable[i*2:i*3]:
        recurrence = i
        break

print(f'Part 2: {scores[((1_000_000_000 + 1) % recurrence) * recurrence - 1]}')
