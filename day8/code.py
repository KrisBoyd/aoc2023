data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()

moves = data[0]
nodes = [s.split(' = ') for s in data[2:]]
nodes = {s[0]: tuple(s[1].replace('(', '').replace(')', '').split(', ')) for s in nodes}

# Part 1
pos = 'AAA'
i = 0
while pos != 'ZZZ':
    m = moves[i % len(moves)]
    j = 0 if m == 'L'  else 1
    pos = nodes[pos][j]
    i += 1

print(f'Part 1: {i}')
       
# Part 2
pos = [s for s in nodes if s.endswith('A')]
repeat = []
for p in pos:
    i = 0
    while p[-1] != 'Z':
        m = moves[i % len(moves)]
        j = 0 if m == 'L'  else 1
        p = nodes[p][j]
        i += 1
    repeat.append(i)

# Find common factors
def factors(n):
    f = []
    for x in range(2, n):
        if n%x == 0:
            f.append(x)
    return f

f = [factors(r) for r in repeat]
f = set([x for y in f for x in y])
ans = 1
for i in f:
    ans *= i
print(f'Part 2: {ans}')
