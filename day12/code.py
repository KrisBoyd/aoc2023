data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
data = [s.split() for s in data]

# Part 1 & 2
PART = 2
if PART == 2:
    data = [['?'.join([s[0]] * 5), ','.join([s[1]] * 5)] for s in data]

def generate_strings(unsolved_strings, a, x, n):
    new_strings = {}
    for s, value in unsolved_strings.items():
        if s.count('#') == n:
            c = s.replace('?', '.')
            if decode_string(c) == x:
                a += value
        elif s.count('#') + s.count('?') == n:
            c = s.replace('?', '#')
            if decode_string(c) == x:
                a += value
        else:
            for char in ['.', '#']:
                new_string = s[:s.find('?')] + char + s[s.find('?')+1:]
                code = decode_string(new_string)
                if '+' in code:
                    code = ','.join(code[:-1].split(',')[:-1])
                if code == x:
                    a += value
                elif x[:len(code)] == code:
                    new_strings[new_string] = value
    if len(new_strings):
        # Group new strings on similarity
        codes = {}
        for s, v in new_strings.items():
            code = decode_string(s)
            if code not in codes:
                codes[code] = [s, v]
            else:
                codes[code][1] += v
        
        new_strings = {k: v for k, v in codes.values()}

        return generate_strings(new_strings, a, x, n)
    else:
        return a


def decode_string(x):
    code = ''
    c = 0
    for i, j in enumerate(x):
        if j == '?':
            if c > 0:
                code += str(c) + '++'
            break
        if j == '#':
            c += 1
        if ((j == '.') or (i == len(x) - 1)) and (c > 0):
            code += str(c) + ','
            c = 0
    return code[:-1]


# Part 1
total_arrangements = 0
for i, (s, x) in enumerate(data):
    arrangements = generate_strings({s: 1}, 0, x, n=sum([int(y) for y in x.split(',')]))
    print(f'{i} - {x} - {arrangements}')
    total_arrangements += arrangements
print(f'Part {PART}: {total_arrangements}')
       