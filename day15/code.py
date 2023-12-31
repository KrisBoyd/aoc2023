from collections import OrderedDict
data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
data = [s for s in data[0].split(',')]


# Part 1
def hash(l):
    v = 0
    for c in l:
        v = (v + ord(c)) * 17 % 256
    return v

print(f'Part 1: {sum([hash(s) for s in data])}')
       
# Part 2
boxes = [OrderedDict() for _ in range(256)]
for s in data:
    operator = '=' if '=' in s else '-'
    label = s[:s.find(operator)]
    box = hash(label)
    if operator == '-':
        boxes[box].pop(label, None)
    elif operator == '=':
        boxes[box][label] = int(s[s.find('=') + 1])

p = 0
for i, b in enumerate(boxes, 1):
    for j, s in enumerate(b.values(), 1):
        p += i * j * s

print(f'Part 2: {p}')
