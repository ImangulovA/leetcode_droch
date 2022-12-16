test = False
if test:
    lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')
else:
    with open('/Users/dev/Downloads/input (13).txt', 'r') as f:
        lines = f.readlines()

if test:
    x1 = 470
    x2 = 525
    y1 = 0
    y2 = 12
else:
    x1 = 300
    x2 = 700
    y1 = 0
    y2 = 160
# p1
# generating massive
sandpoint = [500-x1,0-y1]
xlen = x2-x1
massive = [['.' for i in range(xlen)] for k in range(y1,y2)]
for li in lines:
    l = li.replace('\n','')
    ls = l.split(' -> ')
    ls = [list(map(int,i.split(','))) for i in ls]
    for k in range(1,len(ls)):
        xl = ls[k][0] - x1
        xr = ls[k-1][0] - x1
        xl,xr = min(xl,xr), max(xl,xr)+1
        yl = ls[k][1] - y1
        yr = ls[k-1][1] - y1
        yl,yr= min(yl,yr), max(yl,yr)+1
        for yi in range(yl,yr):
            for xi in range(xl,xr):
                massive[yi][xi]='#'
        #print(xl,xr,yl,yr)

    #print(ls)
#
# for m in massive:
#     print(''.join(m))
# line for p2
massive[-1] = ['#' for i in range(xlen)]
# for m in massive:
#     print(''.join(m))
#sandfall
sch = True
sandcount = 0
while sch:
    sandpos = sandpoint.copy()
    fallingcont = True
    while fallingcont:
        if sandpos[1]==y2-1:
            fallingcont=False
            sch=False
        elif massive[sandpos[1]+1][sandpos[0]] == '.':
            sandpos[1] += 1
        elif massive[sandpos[1]+1][sandpos[0]-1] == '.':
            sandpos[1] += 1
            sandpos[0] -= 1
            #print('hui')
        elif massive[sandpos[1]+1][sandpos[0]+1] == '.':
            sandpos[1] += 1
            sandpos[0] += 1
            #print('hui')
        else:
            fallingcont = False
            #print(sandpos)
            massive[sandpos[1]][sandpos[0]] = 'o'
            sandcount+=1
            if sandpos==sandpoint:
                sch=False
            #print(sandcount)

print(sandcount)
# for m in massive:
#     print(''.join(m))