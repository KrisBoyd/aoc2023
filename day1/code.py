data = open("day1/data.txt", "r").read().splitlines()
print(data)

# Part 1
res = [0] * len(data)
for i, s in enumerate(data):
    for c in s:
        if c in '123456789':
            res[i] = c
            break
    for c in reversed(s):
        if c in '123456789':
            res[i] += c
            break

print('Part 1:')
print(sum([int(s) for s in res]))

# Part 2
numbers = {'one': '1',
           'two': '2',
           'three': '3',
           'four': '4',
           'five': '5',
           'six': '6',
           'seven': '7',
           'eight': '8',
           'nine': '9'}

res = [None] * len(data)
for i, s in enumerate(data):
    res[i] = {}
    # Find numbers
    for j, c in enumerate(s):
        if c in '123456789':
            res[i][j] = c
    # Find letters
    for n in numbers:
        if n in s:
            res[i][s.find(n)] = numbers[n]
            res[i][s.rfind(n)] = numbers[n]


print('Part 2:')
print(sum([int(s[min(s.keys())] + s[max(s.keys())]) for s in res]))

