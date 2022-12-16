test = False
import time
if test:
    lines = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split('\n')
else:
    with open('/Users/dev/Downloads/input (15).txt', 'r') as f:
        lines = f.readlines()

# p1
s = []
b = []
ds = []
valves = {}
frs = []
svd = {}
cntr = 0
for li in lines:
    l = li.replace('\n','')
    ls = l.split(' ')
    vn = ls[1]
    fr = int(ls[4].split('=')[1][:-1])
    cons = [i.replace(',','') for i in ls[9:]]
    valves[vn] = {'fr':fr,'cons':cons}
    #print(vn,fr,cons)
    frs.append(fr)
    svd[vn] = cntr
    cntr+=1

valvestime = [[100 for i in range(len(valves))] for i in range(len(valves))]
for v in valves:
    #print(v)
    valvestime[(svd[v])][svd[v]]=0
    for c in valves[v]['cons']:
        valvestime[(svd[v])][svd[c]]=1
sch = True
while sch:
    sch = False
    for y in range(len(valvestime)-1):
        for x in range(y+1,len(valvestime[0])):
            if 1>0:
                for z in range(len(valvestime)):
                    if (z!=x) & (z!=y):
                        if valvestime[y][x] > (valvestime[y][z] + valvestime[z][x]):
                            valvestime[y][x] = valvestime[y][z] + valvestime[z][x]
                            valvestime[x][y] = valvestime[y][z] + valvestime[z][x]
                            sch = True

# for v in valvestime:
#     print(v)
tl = 30
curlocked = [True for i in range(len(valves))]
curloc = 0
def vwayopt(tl, curloc, curlocked):
    if tl == 0:
        return 0
    if sum(curlocked)==0:
        return 0
    possibilities = [max((tl-valvestime[curloc][i]-1)*frs[i]*curlocked[i],0) for i in range(len(valves))]
    for i in range(len(valves)):
        if possibilities[i]!=0:
            possibilities[i] +=\
                vwayopt(tl-valvestime[curloc][i]-1, i, curlocked[:i] + [False] + curlocked[(i+1):])

    return max(possibilities)
# for v in valvestime:
#     print(v)
def vwayopt2(tl, curloc,curloc2, tl2, curlocked):
    if tl == 0:
        return 0
    if sum(curlocked)==0:
        return 0
    possibilities = [max((tl-valvestime[curloc][i]-1)*frs[i]*curlocked[i],0) for i in range(len(valves))]
    elpossibilities = [max((tl2-valvestime[curloc2][i]-1)*frs[i]*curlocked[i],0) for i in range(len(valves))]
    difpos = [[0 for k in range(len(valves))] for k2 in range(len(valves))]
    for i in range(len(valves)):
        for i2 in range(len(valves)):
            if (i2 != i) & curlocked[i] & curlocked[i2]:
                if possibilities[i]>0:
                    if elpossibilities[i2]>=0:
                        difpos[i2][i] = possibilities[i] + \
                                        elpossibilities[i2] +\
                                        vwayopt2(tl-valvestime[curloc][i]-1, i,
                                     i2,
                                                 tl2-(valvestime[curloc2][i2])-1,
                                     curlocked[:(min(i,i2))] + [False] + curlocked[(min(i,i2)+1):(max(i,i2))] + [False] + curlocked[(max(i,i2)+1):])

    return max(max(difpos))

start_time = time.time()
print(vwayopt2(6, svd['AA'],svd['AA'],6, [True for i in range(len(valves))]))
elapsed_time = time.time() - start_time
print(elapsed_time)
print(vwayopt2(16, svd['AA'],svd['AA'],16, [True for i in range(len(valves))]))
elapsed_time = time.time() - start_time
print(elapsed_time)
print(vwayopt2(26, svd['AA'],svd['AA'],26, [True for i in range(len(valves))]))
elapsed_time = time.time() - start_time
print(elapsed_time)

