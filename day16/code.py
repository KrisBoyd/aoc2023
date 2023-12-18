data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()

# Part 1
move = {'right': (0, 1),
        'left': (0, -1),
        'up': (-1, 0),
        'down': (1, 0)}

def next_step(data, move, p, m):
    p = (p[0] + move[m][0], p[1] + move[m][1])
    if not ((0 <= p[0] < len(data)) and (0 <= p[1] < len(data[0]))):
        return None
    s = data[p[0]][p[1]]
    if s == '.':
        pass
    elif s == '\\':
        if m == 'right':
            m = 'down'
        elif m == 'up':
            m = 'left'
        elif m == 'down':
            m = 'right'
        elif m == 'left':
            m = 'up'
    elif s == '/':
        if m == 'right':
            m = 'up'
        elif m == 'up':
            m = 'right'
        elif m == 'down':
            m = 'left'
        elif m == 'left':
            m = 'down'
    elif s == '|':
        if m in ['down', 'up']:
            pass
        else:
            m = ('down', 'up')
    elif s == '-':
        if m in ['left', 'right']:
            pass
        else:
            m = ('left', 'right')
    m = m if type(m) is tuple else tuple([m])
    return p, m

def calculate_energy(data, move, PART):
    if PART == 1:
        starters =[((0, -1), tuple(['right']))]
    else:
        starters = [((i, -1), tuple(['right'])) for i in range(len(data))] + \
            [((i, len(data[0])), tuple(['left'])) for i in range(len(data))] + \
            [((-1, i), tuple(['down'])) for i in range(len(data[0]))] + \
            [((-1, len(data)), tuple(['up'])) for i in range(len(data[0]))]

    best = 0
    for start in starters:
        steps = [start]
        all_steps = set([])
        while len(steps):
            next_gen = []
            for step in steps:
                for m in step[1]:
                    new_step = next_step(data, move, p=step[0], m=m)
                    if new_step is not None:
                        next_gen += [new_step]
            steps = list(set(next_gen) - set(all_steps))
            all_steps = set(list(all_steps) + next_gen)
        best = max(best, len(set([s[0] for s in all_steps])))

    print(f'Part {PART}: {best}')

calculate_energy(data, move, 1)
calculate_energy(data, move, 2)
