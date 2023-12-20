from copy import deepcopy
data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
data = [s.split(' -> ') for s in data]

mods = {}
for x in data:
    t = x[0][0]
    if t == '%':
        status = 'off'
    elif t == '&':
        status = {m[0].replace('%', '').replace('&', ''): 'low' for m in data if x[0][1:] in m[1].split(',')}
    else:
        status = t
    mods[x[0].replace('%', '').replace('&', '')] = (t, x[1].split(', '), status)

# Part 1
m = deepcopy(mods)

# Part 2
cycle_node = [k for k, v in m.items() if v[1] == ['rx']][0]
cycles = {k: 0 for k in m[cycle_node][2].keys()} 

count = {'low': 0, 'high': 0}
i = 0
while i < 10_000:
    i += 1
    signals = [('broadcaster', 'low', 'push')]  # module, pulse, source
    while signals:
        new_signals = []
        for s in signals:
            count[s[1]] += 1
            if s[0] not in m:
                continue
            # Part 2
            if s[0] == cycle_node and s[1] == 'high':
                if cycles[s[2]] == 0:
                    cycles[s[2]] = i              
                if all([v > 0 for v in cycles.values()]):
                    r = 1
                    for v in cycles.values():
                        r *= v
                    print(f'Part 2: {r}')
                    i = 10_000
                    break
            
            mod = m[s[0]]
            if mod[0] == 'b':
                pulse = s[1]
            elif mod[0] == '%':
                if s[1] == 'high':
                    continue
                else:
                    status = 'off' if m[s[0]][2] == 'on' else 'on'
                    pulse = 'high' if status == 'on' else 'low'
                    m[s[0]] = (m[s[0]][0], m[s[0]][1], status)
            elif mod[0] == '&':
                m[s[0]][2][s[2]] = s[1]
                pulse = 'low' if all([r == 'high' for r in mod[2].values()]) else 'high'
                
            for new_s in mod[1]:
                new_signals += [(new_s, pulse, s[0])]

        signals = new_signals
    if i == 1000:
        print(f"Part 1: {count['low'] * count['high']}")
