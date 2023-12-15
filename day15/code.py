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
        if label in boxes[box]:
            del boxes[box][label]
    elif operator == '=':
        focal_length = int(s[s.find('=') + 1])
        boxes[box][label] = focal_length

p = 0
for i, b in enumerate(boxes):
    for j, s in enumerate(b.values()):
        p += (i+1) * (j+1) * s

print(f'Part 2: {p}')
