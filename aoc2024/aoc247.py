s1 = 0
s2 = 0

prod = True

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_7.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split("""
""")

def ifican(a,b,answ):
    if len(b) == 0:
        return a == answ
    else:
        apb = answ+b[0]
        # if apb > a:
        #     return False
        plus = ifican(a, b[1:], apb)
        amb = answ*b[0]
        # if amb > a:
        #     return False
        mup = ifican(a,b[1:], amb)
        # for part 1:
        # return plus or mup

        # for part 2:
        acb = int(str(answ) + str(b[0]))
        con = ifican(a,b[1:], acb)
        return plus or mup or con

for line in lines:
    # print(line)
    a, b = line.split(': ')
    a = int(a)
    b = list(map(int, b.split(' ')))
    # print(a,b)
    if ifican(a,b[1:], b[0]):
        print(a,b)
        s1+=a
print(s1)
print(s2)
