data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()

# Part 1 & 2
def calculate_distance(data, expansion=1):
    distance = 0
    galaxies = []
    empty_rows = set(range(len(data)))
    empty_cols = set(range(len(data[0])))
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == '#':
                galaxies.append((i, j))
                empty_rows -= {i}
                empty_cols -= {j}

    while len(galaxies):
        g = galaxies.pop(0)
        for h in galaxies:
            distance += abs(h[0] - g[0]) + abs(h[1] - g[1])
            distance += (len([r for r in empty_rows if min(g[0], h[0]) < r < max(g[0], h[0])]) * expansion)
            distance += (len([r for r in empty_cols if min(g[1], h[1]) < r < max(g[1], h[1])]) * expansion)
    return distance

print(f'Part 1: {calculate_distance(data, expansion=1)}')
print(f'Part 2: {calculate_distance(data, expansion=999_999)}')
