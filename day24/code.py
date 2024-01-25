data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
data = [[[int(y) for y in x.split(', ')] for x in s.split(' @ ')] for s in data]


# Part 1
a = 200000000000000
b = 400000000000000

paths = []
for s in data:
    slope = s[1][1] / s[1][0]
    c = s[0][1] - s[0][0] * slope
    paths.append((s, slope, c))

crosses = 0
for i, x in enumerate(paths[:-1]):
    print(x)
    for y in paths[(i+1):]:
        if x[1] == y[1]:
            continue
        cross_x = (y[2] - x[2]) / (x[1] - y[1])
        cross_y = x[1] * cross_x + x[2]
        if (a <= cross_x <= b) and (a <= cross_y <= b):
            # check if past
            if (x[0][1][0] < 0) and (x[0][0][0] < cross_x):
                continue
            if (y[0][1][0] < 0) and (y[0][0][0] < cross_x):
                continue
            if (x[0][1][0] > 0) and (x[0][0][0] > cross_x):
                continue
            if (y[0][1][0] > 0) and (y[0][0][0] > cross_x):
                continue
            print(f'\t {y} - crossed!')
            crosses += 1
        else:
            print(f'\t {y} - not crossed')
print(f'Part 1: {crosses}')
       
# Part 2
"""
(dy'-dy) X + (dx-dx') Y + (y-y') DX + (x'-x) DY = x' dy' - y' dx' - x dy + y dx
(dz'-dz) X + (dx-dx') Z + (z-z') DX + (x'-x) DZ = x' dz' - z' dx' - x dz + z dx
(dy'-dy) Z + (dz-dz') Y + (y-y') DZ + (z'-z) DY = z' dy' - y' dz' - z dy + y dz 
"""
# 3 rocks collide with an unknown 4th rock. 
# Calculate the time of collision for the first rock.
def collision(data):
    (x1, y1, z1), (vx1, vy1, vz1) = data[0]
    (x2, y2, z2), (vx2, vy2, vz2) = data[1]
    (x3, y3, z3), (vx3, vy3, vz3) = data[2]
    
    yz = y1*(z2 - z3) + y2*(-z1 + z3) + y3*(z1 - z2)
    xz = x1*(-z2 + z3) + x2*(z1 - z3) + x3*(-z1 + z2)
    xy = x1*(y2 - y3) + x2*(-y1 + y3) + x3*(y1 - y2)
    vxvy = vx1*(vy2 - vy3) + vx2*(-vy1 + vy3) + vx3*(vy1 - vy2)
    vxvz = vx1*(-vz2 + vz3) + vx2*(vz1 - vz3) + vx3*(-vz1 + vz2)
    vyvz = vy1*(vz2 - vz3) + vy2*(-vz1 + vz3) + vy3*(vz1 - vz2)

    n = (vx2 - vx3)*yz + (vy2 - vy3)*xz + (vz2 - vz3)*xy
    d = (z2 - z3)*vxvy + (y2 - y3)*vxvz + (x2 - x3)*vyvz
    
    return n / d

t1 = collision(data)
t2 = collision([data[1], data[0], data[2]])

c1 = [x + v*t1 for x, v in zip(*data[0])]
c2 = [x + v*t2 for x, v in zip(*data[1])]
v = [(x2 - x1) / (t2 - t1) for x1, x2 in zip(c1, c2)]
p = [x + pv*t1 - vv*t1 for x, pv, vv in zip(*data[0], v)]

print(f'Part 2: {sum(p)}')

   

