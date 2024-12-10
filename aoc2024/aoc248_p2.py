import copy

s1 = 0
s2 = 0

prod = True

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_8.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".split("""
""")

radios = {}
bi = len(lines)
bk = len(lines[1])

for i, line in enumerate(lines):
    # print(line)
    for k, ele in enumerate(line):
        if ele.isalpha() or ele.isdigit():
           if ele in radios:
               radios[ele].append([i,k])
           else:
               radios[ele] = [[i,k]]


def inbound(point):
    boundx = (point[0] >= 0) and (point[0] < bi)
    boundy = (point[1] >= 0) and (point[1] < bk - 1)
    return (boundx and boundy)

antinodes = []

for key, value in radios.items():
    print(key, value)
    if len(value) >= 2:
        for iter in range(len(value)):
            for kiter in range(iter+1,len(value)):
                dif = [value[iter][0] - value[kiter][0], value[iter][1]-value[kiter][1]]
                inbnd = True
                a1 = copy.deepcopy(value[iter])
                while inbnd:
                    if inbound(a1):
                        antinodes.append(a1)
                    else:
                        inbnd = False
                    a1 = [a1[0]+dif[0], a1[1]+dif[1]]
                inbnd = True
                a1 = copy.deepcopy(value[iter])
                a1 = [a1[0] - dif[0], a1[1] - dif[1]]
                while inbnd:
                    if inbound(a1):
                        antinodes.append(a1)
                    else:
                        inbnd = False
                    a1 = [a1[0] - dif[0], a1[1] - dif[1]]

print(len(antinodes))
setantinodes = set(list(set(map(tuple, antinodes))))
print(len(setantinodes))
print(setantinodes)
#
# print(s1)
# print(s2)
