

with open('/Users/dev/Downloads/input (3).txt', 'r') as f:
  lines = f.readlines()
ec = 0
ec2 = 0
for l in lines:
    [e1, e2] = l.split(',')
    b1 = list(map(int, e1.split('-')))
    b2 = list(map(int, e2.split('-')))
    if (b1[0] <= b2[0]) & (b1[1]>= b2[1]):
        ec+=1
    elif (b1[0] >= b2[0]) & (b1[1]<= b2[1]):
        ec+=1
    if (b1[0] >= b2[0]) & (b1[0] <= b2[1]):
        ec2+=1
    elif (b1[1] >= b2[0]) & (b1[1] <= b2[1]):
        ec2+=1
    elif (b2[0] >= b1[0]) & (b2[0] <= b1[1]):
        ec2+=1
    elif (b2[1] >= b1[0]) & (b2[1] <= b1[1]):
        ec2+=1

print(ec)
print(ec2)
