test = True
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

def listcomp(l,r):


for i in range(0,len(lines),3):
    l = lines[i]
    r = lines[i+1]
    print(l,r)