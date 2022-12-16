test = False
if test:
    lines = """30373
25512
65332
33549
35390""".split('\n')
else:
    with open('/Users/dev/Downloads/input (7).txt', 'r') as f:
        lines = f.readlines()

forest = []
for li in lines:
    l = li.replace('\n','')
    forest.append(list(map(int,list(l))))

print(len(forest[0]))
print(len(forest))

vistrees = len(forest[0]) * 2 + len(forest) * 2 - 4
sc = 0
for i in range(1,len(forest)-1):
    for k in range(1,len(forest[0])-1):
        # vis = True
        ot = forest[i][k]
        d1 = max(forest[i][:k])
        d2 = max(forest[i][(k+1):])
        d3 = max([forest[j][k] for j in range(0,i)])
        d4 = max([forest[j][k] for j in range(i+1, len(forest))])
        around = [d1,d2,d3,d4]
        if ot > min(around):
            vistrees += 1
        #print(i,k,ot,around,min(around))
        t1, t2, t3, t4 = True, True, True, True
        sc1 = 0
        while t1:
            sc1+=1
            if k-sc1 == 0:
                t1 = False
            else:
                if forest[i][(k-sc1)] >= ot:
                    t1 = False
        sc2 = 0
        while t2:
            sc2+=1
            if k+sc2 == len(forest[i]) - 1:
                t2 = False
            else:
                if forest[i][(k+sc2)] >= ot:
                    t2 = False
        sc3 = 0
        while t3:
            sc3 += 1
            if i - sc3 == 0:
                t3 = False
            else:
                if forest[i-sc3][(k)] >= ot:
                    t3 = False
        sc4 = 0
        while t4:
            sc4 += 1
            if i + sc4 == len(forest) - 1:
                t4 = False
            else:
                if forest[i+sc4][(k)] >= ot:
                    t4 = False

        if sc1*sc2*sc3*sc4 > sc:
            sc = sc1*sc2*sc3*sc4
            print(sc,i,k, sc1, sc2, sc3, sc4)


print(vistrees)