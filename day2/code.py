data = open("day2/data.txt", "r").read().splitlines()
print(data)

# Part 1 [12 red, 13 green, 14 blue]
fail = 0
for idx, s in enumerate(data):
   s = s.split(': ')[1].replace(';', ',')
   for x in s.split(', '):
        value, color = x.split(' ')
        if (color == 'red' and int(value) > 12) or \
           (color == 'green' and int(value) > 13) or \
           (color == 'blue' and int(value) > 14):
            fail += (idx + 1)
            break      

print('Part 1:')
print(len(data) * (len(data) + 1) // 2 - fail)

# Part 2
res = 0
for idx, s in enumerate(data):
   s = s.split(': ')[1].replace(';', ',')
   power = [0, 0, 0]
   for x in s.split(', '):
        value, color = x.split(' ')
        if color == 'red':
            power[0] = max(power[0], int(value))
        if color == 'green':
            power[1] = max(power[1], int(value))
        if color == 'blue':
            power[2] = max(power[2], int(value))
   res += power[0] * power[1] * power[2]

print(f'Part 2: {res}')

