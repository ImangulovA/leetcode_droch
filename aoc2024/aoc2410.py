s1 = 0
s2 = 0

prod = True

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_10.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split("""
""")

wherecanigo = {}
zeros = []
bi = len(lines)
bk = len(lines[0])
for i, line in enumerate(lines):
    # print(line)
    for k, ele in enumerate(line):
        if ele == '0':
            zeros.append([i,k])
        if ele != '9' and ele != '\n':
            ep = str(int(ele)+1)
            # print(ele, ep)
            ns = []
            if i > 0:
                if lines[i-1][k] == ep:
                    ns.append([i-1, k])
            if i < bi - 1:
                if lines[i+1][k] == ep:
                    ns.append([i+1, k])
            if k > 0:
                if lines[i][k-1] == ep:
                    ns.append([i, k-1])
            if k < bk - 1:
                if lines[i][k+1] == ep:
                    ns.append([i, k+1])
            wherecanigo[tuple([i,k])] = ns
# print(wherecanigo)
for z in zeros:
    ns = list(set(map(tuple, [z])))
    for iter in range(9):
        # print(ns)
        nns = []
        for n in ns:
            nns.extend(wherecanigo[tuple(n)])
        # for part 1
        ns = set(list(set(map(tuple, nns))))
        # for part 2
        ns = nns
    print(len(ns), ns)
    s1+=len(ns)
#
#
# for line in lines:
#     print(line)
print(s1)
print(s2)
