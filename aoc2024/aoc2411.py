s1 = 0
s2 = 0

prod = True

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_11.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """125 17""".split("""
""")

for line in lines:
    print(list(map(int,line.split(' '))))
    stns = list(map(int,line.split(' ')))
    for i in range(75):
        nstns = []
        for stn in stns:
            if stn == 0:
                nstns.append(1)
            else:
                if len(str(stn)) % 2 == 0:
                    nstns.append(int(str(stn)[:len(str(stn))//2]))
                    nstns.append(int(str(stn)[(len(str(stn)) // 2):]))
                else:
                    nstns.append(stn*2024)
        stns = nstns
        print(i+1, len(stns))
print(s1)
print(s2)
