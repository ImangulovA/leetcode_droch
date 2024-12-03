import re
s1 = 0
s2 = 0

p1 = "mul\([0-9]{1,3},[0-9]{1,3}\)"
p2 = "[0-9]{1,3}"

pdn = "don't\(\)"
pd = "do\(\)"

prod = True

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_3.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

line = ''.join(lines)

x = re.finditer(p1, line)

ydn = re.finditer(pdn, line)
yd = re.finditer(pd, line)
ydn = ([m.start(0) for m in ydn])
yd = ([m.start(0) for m in yd])
for i in x:
    nums = re.findall(p2,i.group())
    nums = list(map(int,nums))
    s1 += nums[0] * nums[1]
    if i.start(0) < min(ydn):
        s2 += nums[0] * nums[1]
    else:
        mydn = max(k for k in ydn if k < i.start(0))
        if i.start(0) > min(yd):
            myd = max(k for k in yd if k < i.start(0))
            if myd > mydn:
                s2 += nums[0] * nums[1]
print(s1)
print(s2)
