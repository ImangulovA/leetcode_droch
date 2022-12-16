test = False
if test:
    lines = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".split('\n')
else:
    with open('/Users/dev/Downloads/input (9).txt', 'r') as f:
        lines = f.readlines()

interesting = []
intsign = [i for i in range(20,221,40)]
x = 1
cycle = 1
printres = []
nl = '#'
#p1
for li in lines:
    l = li.replace('\n','')
    ls = l.split(' ')
    if ls[0] == 'noop':
        cycle += 1
        if cycle in intsign:
            #print(ls)
            interesting.append(x*cycle)
    if ls[0] == 'addx':
        cycle += 1
        if cycle in intsign:
            #print(ls)
            interesting.append(x*cycle)
        cycle += 1
        #print(x,ls[1])
        x += int(ls[1])
        if cycle in intsign:
            #print(ls)
            interesting.append(x*cycle)
print(sum(interesting))
print(interesting)

#p2
cycle = 0
x = 1
intsign = [i for i in range(0,221,40)]
for li in lines:
    l = li.replace('\n','')
    ls = l.split(' ')
    if ls[0] == 'noop':
        cycle += 1
        if cycle in intsign:
            printres.append(nl)
            nl = ''
        if abs((cycle%40)-x) < 2:
            nl+='#'
        else:
            nl+='.'

    if ls[0] == 'addx':
        cycle += 1
        if cycle in intsign:
            printres.append(nl)
            nl = ''
        if abs((cycle % 40) - x) < 2:
            nl += '#'
        else:
            nl += '.'

        cycle += 1
        x += int(ls[1])

        if cycle in intsign:
            printres.append(nl)
            nl = ''
        if abs((cycle%40)-x) < 2:
            nl+='#'
        else:
            nl+='.'
printres.append(nl)

for l in printres:
    print(l)
