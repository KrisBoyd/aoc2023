from copy import deepcopy
data = open(__file__.replace('code.py', 'data.txt'), "r").read()
workflow, parts = [s.split('\n') for s in data.split('\n\n')]

wf = {}
for w in workflow:
    name, i = w.replace('}', '').split('{') 
    wf[name] = [j.split(':') for j in i.split(',')]

parts = [eval(p.replace("=", "':").replace(",", ",'").replace("{", "{'")) for p in parts]

# Part 1
res = 0
for p in parts:
    name = 'in'
    ans = None
    while not ans:
        for i in wf[name]:
            if len(i) == 2:
                eq = i[0]
                eq = eq.replace(eq[0], str(p[eq[0]]))
                if eval(eq):
                    if i[1] in ['A', 'R']:
                        ans = i[1]
                    else:
                        name = i[1]
                    break
            else:
                if i[0] in ['A', 'R']:
                    ans = i[0]
                else:
                    name = i[0]
                break
    if ans == 'A':
        res += sum(p.values())

print(f'Part 1: {res}')

# Part 2
unsolved = [[{'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, ('in', 0)]]

def solve_parts(unsolved, solved, wf):
    new_unsolved = []
    for u in unsolved:
        part = u[0]
        i = wf[u[1][0]][u[1][1]]
        if len(i) == 2:
            v = int(i[0][2:])
            eq = i[0][1]
            bounds = part[i[0][0]]
            if eq == '<':
                if bounds[0] < v:
                    new = deepcopy(u)
                    new[0][i[0][0]] = [bounds[0], min(v - 1, bounds[1])]
                    new[1] = (i[1], 0)
                    if new[1][0] in ['R', 'A']:
                        solved.append(new)
                    else:
                        new_unsolved.append(new)
                    
                    if v <= bounds[1]:
                        new = deepcopy(u)
                        new[0][i[0][0]] = [v, bounds[1]]
                        new[1] = (new[1][0], new[1][1] + 1)
                        new_unsolved.append(new)
            elif eq == '>':
                if bounds[1] > v: # true
                    new = deepcopy(u)
                    new[0][i[0][0]] = [max(v + 1, bounds[0]), bounds[1]]
                    new[1] = (i[1], 0)
                    if new[1][0] in ['R', 'A']:
                        solved.append(new)
                    else:
                        new_unsolved.append(new)
                
                    if v >= bounds[0]: # false
                        new = deepcopy(u)
                        new[0][i[0][0]] = [bounds[0], v]
                        new[1] = (new[1][0], new[1][1] + 1)
                        new_unsolved.append(new)
        else:
            new = deepcopy(u)
            new[1] = (i[0], 0)
            if new[1][0] in ['R', 'A']:
                solved.append(new)
            else:
                new_unsolved.append(new)

    if len(new_unsolved):
        return solve_parts(new_unsolved, solved, wf)
    else:
        return solved

solved = solve_parts(unsolved, solved=[], wf=wf)
solved = [list(s[0].values()) for s in solved if s[1][0] == 'A']
v = 0
for s in solved:
    a = 1
    for j in s:
        a *= (j[1] - j[0] + 1)
    v += a
print(f'Part 2: {v}')
