data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
data = [[int(x) for x in s.split()] for s in data]

# Part 1
t = 0
for s in data:
    e = 0
    d = s
    while d.count(0) != len(d):
        e += d[-1]
        d = [x - y for x, y in zip(d[1:], d[0:-1])]
    t += e
print(f'Part 1: {t}')
       
# Part 2
t = 0
for s in data:
    e = []
    d = s
    while d.count(0) != len(d):
        e.append(d[0])
        d = [x - y for x, y in zip(d[1:], d[0:-1])]
    v = 0
    for j in reversed(e):
        v = j - v
    t += v

print(f'Part 2: {t}')