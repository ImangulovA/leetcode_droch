s1 = 0
s2 = 0
list_1 = []
list_2 = []
with open('C:/Users/Amal Imangulov/Downloads/input.txt', 'r') as f:
    for line in f:
        i,k = list(map(int, line.split('   ')))
        list_1.append(i)
        list_2.append(k)

list_1.sort()
list_2.sort()

for i in range(len(list_1)):
    s1+=abs(list_2[i] - list_1[i])
    print(s1)
    s2+=list_1[i]*list_2.count(list_1[i])

print(s1)
print(s2)
