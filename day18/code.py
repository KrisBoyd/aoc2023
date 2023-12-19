data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
data = [s.split(' ') for s in data]


# Part 1
def find_surface(data):
    moves = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}
    p = (0, 0)
    v = 0
    for d in data:
        p_new = (p[0] + moves[d[0]][0] * int(d[1]), p[1] + moves[d[0]][1] * int(d[1]))
        v += (p[0] * p_new[1] - p[1] * p_new[0])
        p = p_new
    v = abs(v) / 2
    perimeter = sum([int(d[1]) for d in data])   
    return int(v + perimeter // 2 + 1)

print(f'Part 1: {find_surface(data)}')

# Part 2
direction = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
data = [d[2][2:-1] for d in data]
data = [(direction[d[-1]], int(d[:-1], 16)) for d in data]
print(f'Part 2: {find_surface(data)}')
