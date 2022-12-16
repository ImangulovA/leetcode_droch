import math
sign = lambda x: math.copysign(1, x)
test = False
if test:
    lines = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split('\n')
else:
    with open('/Users/dev/Downloads/input (8).txt', 'r') as f:
        lines = f.readlines()

# p1
headco = tuple([0,0])
tailco = tuple([0,0])
tcos = {tuple([0,0]):1}

for li in lines:
    l = li.replace('\n','')
    i, k = l.split(' ')
    k = int(k)
    if i == 'R':
        cco = [1, 0]
    elif i == 'L':
        cco = [-1, 0]
    elif i == 'U':
        cco = [0, 1]
    elif i == 'D':
        cco = [0, -1]
    cco = tuple(cco)
    for _ in range(k):
        phc = headco
        headco = [phc[0]+cco[0], phc[1]+cco[1]]
        if (abs(tailco[0]-headco[0]) > 1) | (abs(tailco[1]-headco[1]) > 1):
            tailco = tuple(phc)
            if tailco in tcos:
                tcos[tailco] += 1
            else:
                tcos[tailco] = 1
        #print(headco, tailco)

#print(tcos)
#print(len(tcos))

# p2
ropeco = [[0,0]]*10
tcos = {tuple([0,0]):1}
for li in lines:
    l = li.replace('\n','')
    i, k = l.split(' ')
    k = int(k)
    if i == 'R':
        cco = [1, 0]
    elif i == 'L':
        cco = [-1, 0]
    elif i == 'U':
        cco = [0, 1]
    elif i == 'D':
        cco = [0, -1]
    # cco = tuple(cco)
    for _ in range(k):
        ropeco[0] = [ropeco[0][0] + cco[0], ropeco[0][1]+cco[1]]
        for j in range(1, len(ropeco)):
            a, b = ropeco[j-1], ropeco[j]
            dx, dy = - ropeco[j][0] + ropeco[j-1][0], - ropeco[j][1] + ropeco[j-1][1]
            if (abs(dx) > 1) | (abs(dy) > 1):
                if dx == 0:
                    ropeco[j] = [ropeco[j][0], ropeco[j][1]+sign(dy)]
                elif dy==0:
                    ropeco[j] = [ropeco[j][0]+sign(dx), ropeco[j][1]]
                else:
                    ropeco[j] = [ropeco[j][0]+sign(dx), ropeco[j][1] + sign(dy)]

        tailco = tuple(ropeco[-1])
        if tailco in tcos:
            tcos[tailco] += 1
        else:
            tcos[tailco] = 1
        #print(headco, tailco)
    print(ropeco)
#print(tcos)
print(len(tcos))
