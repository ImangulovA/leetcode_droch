test = False
if test:
    lines = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split('\n')
else:
    with open('/Users/dev/Downloads/input (12).txt', 'r') as f:
        lines = f.readlines()

#I stole Parser from Reddit, because I HATE WRITING PARSERS

def parse(expr):
    stack = []
    current = []

    parsing_number = False

    for char in expr:
        if parsing_number and not char.isdigit():
            number = int("".join(current))
            current = stack.pop()
            current.append(number)
            parsing_number = False

        if char.isdigit():
            if not parsing_number:
                parsing_number = True
                stack.append(current)
                current = []
            current.append(char)
        elif char == "[":
            stack.append(current)
            current = []
        elif char == "]":
            tmp = current
            current = stack.pop()
            current.append(tmp)


    return current[0]

def compnum(l,r):
    if l == r:
        return None
    return l < r

def comparison(l,r):
    iter = min(len(l),len(r))
    for i in range(iter):
        if (type(l[i])==type(int())) & (type(r[i])==type(int())):
            c = compnum(l[i], r[i])
            if None != c:
                return c
        elif (type(l[i])==type(list())) & (type(r[i])==type(list())):
            c = comparison(l[i], r[i])
            if None != c:
                return c
        elif (type(l[i])==type(int())) & (type(r[i])==type(list())):
            c = comparison([l[i]],r[i])
            if None != c:
                return c
        elif (type(l[i])==type(list())) & (type(r[i])==type(int())):
            c = comparison(l[i],[r[i]])
            if None != c:
                return c
    if len(l) != len(r):
        return len(l) < len(r)
    else:
        return None



p1s = 0
sep1 = [[2]]
sep2 = [[6]]
packlist = [[[2]],[[6]]]
for i in range(0,len(lines),3):
    l = lines[i]
    r = lines[i+1]
    pl = (parse(l))
    pr = (parse(r))
    cmpr = comparison(pl,pr)
    if cmpr:
        p1s+=(i//3 + 1)
        packlist.append(pl)
        packlist.append(pr)
    else:
        packlist.append(pr)
        packlist.append(pl)

#print(packlist)
print(p1s)
allissorted = False
lp = len(packlist)
while allissorted == False:
    allissorted = True
    for i in range(lp-1):
        for k in range(i+1, lp):
            if comparison(packlist[i],packlist[k])==False:
                allissorted=False
                packlist[i], packlist[k] = packlist[k], packlist[i]
div1=(packlist.index(sep1))+1
div2=(packlist.index(sep2))+1
print(div1*div2)


