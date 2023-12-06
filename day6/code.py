data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()

def ways_to_win(time, distance, res=1):
    for t in range(1, time):
        d = t * (time - t)
        if d > distance:
            return res * (time - 2*t + 1)

# Part 1
races = list(zip([int(x) for x in data[0].split(' ')[1:] if x != ''], 
                 [int(x) for x in data[1].split(' ')[1:] if x != '']))
res = 1
for time, distance in races:
    res = ways_to_win(time, distance, res)
print(f'Part 1: {res}')
       
# Part 2
time = int(''.join([x for x in data[0] if x.isdigit()]))
distance = int(''.join([x for x in data[1] if x.isdigit()]))
print(f'Part 2: {ways_to_win(time, distance)}')
