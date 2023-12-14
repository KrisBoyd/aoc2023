data = open(__file__.replace('code.py', 'data.txt'), "r").read().split('\n\n')
data = [s.splitlines() for s in data]

def transform_list(l):
    n, m = len(l), len(l[0])
    t = []
    for j in range(m):
        t.append('')
        for i in range(n):
            t[j] += l[i][j]
    return t

def check_mirrors(pattern, value=1, line=None):
    for m in range(1, len(pattern)):
        if (m * value) == line:
            continue
        w = min(m, len(pattern) - m)      
        l = pattern[m-w:m]
        r = pattern[m:m+w]
        r.reverse()
        if l == r:
            return m * value

# Part 1
res = []
for p in data:
    m = check_mirrors(p, value=100)
    if m is None:
        t = transform_list(p)
        m = check_mirrors(t)
    res += [m]

print(f'Part 1: {sum(res)}')
       
# Part 2
total = 0
for p, line in list(zip(data, res)):
    i = 0
    while True:
        col = i % len(p[0])
        row = i // len(p[0])
        # Adjust one element of the pattern
        rep = '#' if p[row][col] == '.' else '.'
        a = [s for s in p]
        a[row] = a[row][:col] + rep + a[row][col+1:]
        
        m = check_mirrors(a, value=100, line=line)
        if m is None:
            t = transform_list(a)
            m = check_mirrors(t, value=1, line=line)
        if m is not None:
            total += m
            break
        i += 1

print(f'Part 2: {total}')
