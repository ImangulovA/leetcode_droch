s1 = 0
s2 = 0

prod = False

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_18.txt', 'r') as f:
        lines = f.readlines()
    gs = 71
else:
    lines = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".split("""
""")
    gs = 7

for line in lines:
    print(line)
print(s1)
print(s2)
