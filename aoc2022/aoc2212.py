test = False
if test:
    lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split('\n')
else:
    with open('/Users/dev/Downloads/input (11).txt', 'r') as f:
        lines = f.readlines()

# p1
ms = []
mtn = []
start, finish = [0,0],[0,0]
for li in lines:
    l = li.replace('\n','')
    ms.append(l)
for k in range(len(ms)):
    if 'S' in ms[k]:
        start = [k, ms[k].find('S')]
    if 'E' in ms[k]:
        finish = [k, ms[k].find('E')]
    mtn.append([ord(i) - ord('a') for i in ms[k].replace('S','a').replace('E','z')])
print(mtn)
print(start)
print(finish)
y = len(mtn)
x = len(mtn[0])
dss = [[10000 for i in range(len(mtn[0]))] for i in range(len(mtn))]
dss[finish[0]][finish[1]] = 0
print(dss)
iter = 0
sch = True
while (dss[start[0]][start[1]] == 10000) & sch:
    sch = False
    iter += 1
    if iter%10 == 0:
        print(iter)
        if iter%1000 == 0:
            for d in dss:
                print(d)
    for i in range(y):
        for k in range(x):
            if 1>0:
                ht = mtn[i][k]
                a,b,c,d=10000,10000,10000,10000
                try:
                    if (mtn[i+1][k]-ht) < 2:
                        a = dss[i+1][k]
                except:
                    a = 10000
                try:
                    if (mtn[i - 1][k] - ht) < 2:
                        b = dss[i-1][k]
                except:
                    b = 10000
                try:
                    if (mtn[i][k+1] - ht) < 2:
                        c = dss[i][k+1]
                except:
                    c = 10000
                try:
                    if (mtn[i][k-1] - ht) < 2:
                        d = dss[i][k-1]
                except:
                    d = 10000
                if (min(a,b,c,d) + 1) < dss[i][k]:
                    dss[i][k] = min(a,b,c,d) + 1
                    sch = True
# for d in dss:
#     print(d)
print(dss[start[0]][start[1]])
sch = True
while sch:
    sch = False
    iter += 1
    if iter%10 == 0:
        print(iter)
        print(dss[start[0]][start[1]])
        if iter%1000 == 0:
            for d in dss:
                print(d)
    for i in range(y):
        for k in range(x):
            if 1>0:
                ht = mtn[i][k]
                a,b,c,d=10000,10000,10000,10000
                try:
                    if (mtn[i+1][k]-ht) < 2:
                        a = dss[i+1][k]
                except:
                    a = 10000
                try:
                    if (mtn[i - 1][k] - ht) < 2:
                        b = dss[i-1][k]
                except:
                    b = 10000
                try:
                    if (mtn[i][k+1] - ht) < 2:
                        c = dss[i][k+1]
                except:
                    c = 10000
                try:
                    if (mtn[i][k-1] - ht) < 2:
                        d = dss[i][k-1]
                except:
                    d = 10000
                if (min(a,b,c,d) + 1) < dss[i][k]:
                    dss[i][k] = min(a,b,c,d) + 1
                    sch = True

mdk = 10000
for i in range(y):
    for k in range(x):
        if mtn[i][k] == 0:
            if dss[i][k] < mdk:
                mdk = dss[i][k]

print(mdk)