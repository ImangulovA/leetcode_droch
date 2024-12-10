s1 = 0
s2 = 0

prod = False

def nextstep(a,b):
    return [a[i]+b[i] for i in range(2)]


if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_6.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split("""
""")
obstacles = []
bi = len(lines)
bk = len(lines[0])
for i, line in enumerate(lines):
    # print(line)
    for k, ele in enumerate(line):
        if ele == '#':
            obstacles.append([i,k])
        if ele == '^':
            guard = [i,k]

guardwas = {}
curdir = 0
directions = [[-1,0], [0,1], [1,0], [0,-1]]
guardwas[tuple(guard)] = 1
inbound = True

while inbound:
    try:
        ns = nextstep(guard,directions[curdir])
        if ns not in obstacles:
            guard = ns
            if tuple(ns) not in guardwas:
                guardwas[tuple(ns)] = 1
        else:
            curdir = (curdir+1)%4
        if (guard[0] >= bi) or (guard[1] >= bk) or (guard[0] < 0) or (guard[1] < 0):
            print(guard)
            print(len(guardwas)-1)
            print('outbound!')
            inbound = False
    except:
        print('outbound!')
        print(guard)
        print(len(guardwas))
        inbound = False