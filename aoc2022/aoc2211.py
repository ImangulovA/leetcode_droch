test = False
if test:
    lines = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".split('\n')
else:
    with open('/Users/dev/Downloads/input (10).txt', 'r') as f:
        lines = f.readlines()


#p1
monkeys = {}
if test:
    divs = [23, 19, 13, 17]
    dp = 1
    for k in divs:
        dp *= k
else:
    divs = [7, 11, 13, 3, 17, 2, 5, 19]
    dp = 1
    for k in divs:
        dp *= k
if test:
    redir = [[3,2],[0,2],[3,1],[1,0]]
else:
    redir = [[2,6],[0,5],[3,4],[7,1],[7,3],[6,0],[4,2],[1,5]]
if test:
    ops = ['x 19','+ 6','sq','+ 3']
else:
    ops = ['x 11', '+ 1','x 7', '+ 3','+ 6','+ 5','sq','+ 7']
queue = []
for li in lines:
    l = li.replace('\n','')
    ls = l.split(' ')
    if 'Starting items' in l:
        items = list(map(int,[i.replace(',','') for i in ls[4:]]))
        #print(items)
        queue.append(items)
    #print(ls)

if test:
    hmm = 4
else:
    hmm = 8

mj = [0]*hmm
for _ in range(10000):
    print(_)
    for i in range(hmm):
        opsi = ops[i]
        while len(queue[i]) > 0:
            pops = queue[i].pop(0)
            if 'sq' in opsi:
                pops = pops*pops
            elif '+' in opsi:
                pops += int(opsi.split(' ')[1])
            elif 'x' in opsi:
                pops *= int(opsi.split(' ')[1])
            pops = pops%dp
            if pops % divs[i] == 0:
                wtg = redir[i][1]
            else:
                wtg = redir[i][0]
            queue[wtg].append(pops)
            mj[i] += 1
print(queue)
mj.sort()
print(mj)
print(mj[-1]*mj[-2])




