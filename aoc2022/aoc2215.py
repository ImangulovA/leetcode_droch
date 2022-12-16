test = False
if test:
    lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split('\n')
else:
    with open('/Users/dev/Downloads/input (14).txt', 'r') as f:
        lines = f.readlines()

# p1
s = []
b = []
ds = []
for li in lines:
    l = li.replace('\n','')
    ls = l.split(' ')
    [x1,y1,x2,y2] = list(map(int,[ls[2][2:-1], ls[3][2:-1], ls[8][2:-1], ls[9][2:]]))
    s.append([x1,y1])
    b.append([x2,y2])
    d = abs(x1-x2) + abs(y1-y2)
    ds.append(d)

if test:
    fy = 10
else:
    fy = 2000000

# zshkv = {}
# for k in range(len(s)):
#     if abs(fy-s[k][1]) <= ds[k]:
#         dm1 = abs(fy-s[k][1])
#         dm2 = ds[k] - dm1
#         for jl in range(-dm2, dm2+1):
#             zshkv[s[k][0]+jl] = 1
#     else:
#         # print(s[k], ds[k])
#         pass

#
# print(len(zshkv))
#
#
#
#
# print(s)
# print(ds)
print(s)
print(ds)

if test:
    lim = 20
else:
    lim = 4000000
zshkv = {}
for i in range(len(s)):
    print(i)
    for k in range(0,ds[i]+1):
        if (s[i][0]-k) in zshkv:
            zshkv[s[i][0]-k].append([s[i][1]-ds[i]+k, s[i][1]+ds[i]-k])
        else:
            zshkv[s[i][0] - k] = [[s[i][1]-ds[i]+k, s[i][1]+ds[i]-k]]
        if (s[i][0]+ k) in zshkv:
            zshkv[s[i][0] + k].append([s[i][1] - ds[i] + k, s[i][1] + ds[i] - k])
        else:
            zshkv[s[i][0] + k] = [[s[i][1] - ds[i] + k, s[i][1] + ds[i] - k]]
# print(zshkv[10])
#         for j in range(0,ds[i]+1-k):
#             zshkv.append((s[i][0]-k) * 4000000 + (s[i][1]-j))
#             zshkv.append((s[i][0]+k) * 4000000 + (s[i][1]-j))
#             zshkv.append((s[i][0]-k) * 4000000 + (s[i][1]+j))
#             zshkv.append((s[i][0]+k) * 4000000 + (s[i][1]+j))
# print('oba')
# # cnt = 0
# for psh in range(lim):
#     for pp in range(lim):
#         # if psh*4000000+pp not in zshkv:
#         #     cnt+=1
#         #     print(psh*4000000+pp)
#         for key in range(len(s)):
#             if abs(s[0]-psh) + abs(s[1]-pp) < ds[key]:
#                 break
# print(cnt)
#
# print(b)
for k in range(0,lim):
    a = zshkv[k]
    a.sort()
    rb = a[0][1]
    for i in range(1,len(a)):
        if a[i][0]<=rb+1:
            rb = max(a[i][1],rb)
        else:
            print(k,rb,a[i])
            break

