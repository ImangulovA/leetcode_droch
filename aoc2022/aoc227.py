

with open('/Users/dev/Downloads/input (6).txt', 'r') as f:
  lines = f.readlines()

# lines = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k""".split('\n')

dirs = {}
curdir = '/'
prevcd = 'None'
for li in lines:
    l = li.replace('\n','')
    sc = l.split(' ')
    if sc[0] == '$':
        if sc[1] == 'cd':
            # print(sc)
            if sc[2] != '..':
                prevcd = curdir
                curdir = curdir + '/' + sc[2]
            else:
                curdir = dirs[curdir]['header']
                prevcd = dirs[curdir]['header']
        elif sc[1] == 'ls':
            pass
        else:
            print(sc)

    else:
        # this is in curdir
        # print(curdir)
        if curdir not in dirs:
            dirs[curdir] = {'dirs':[], 'files':[],
                            'header':prevcd,'size':-1}
        if sc[0] == 'dir':
            dirs[curdir]['dirs'].append(curdir + '/' + sc[1])
        else:
            dirs[curdir]['files'].append(int(sc[0]))

print(dirs)

werenotdone = True
cntr = 0
while werenotdone:
    cntr+=1
    print(cntr)
    werenotdone = False
    for d in dirs.keys():
        can_i = True
        if len(dirs[d]['dirs']) == 0:
            if len(dirs[d]['files']) != 0:
                dirs[d]['size'] = sum(dirs[d]['files'])
            else:
                dirs[d]['size'] = 0
        else:
            for ind in dirs[d]['dirs']:
                if dirs[ind]['size']==-1:
                    can_i = False
            if can_i:
                ns = 0
                for ind in dirs[d]['dirs']:
                    ns += dirs[ind]['size']
                ns += sum(dirs[d]['files'])
                dirs[d]['size'] = ns
            else:
                werenotdone = True

    if cntr >= 10000:
        for d in dirs.keys():
            print(d, dirs[d]['size'])

p1_ans = 0
for d in dirs.keys():
    if dirs[d]['size'] <= 100000:
        p1_ans += dirs[d]['size']
print(p1_ans)
print(dirs)


space = dirs['///']['size']
needtodel = 30000000-(70000000-space)

p2 = []
for d in dirs.keys():
    if dirs[d]['size'] >= needtodel:
        p2.append(dirs[d]['size'])

print(p2)
print(min(p2))

