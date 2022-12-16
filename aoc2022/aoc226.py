

with open('/Users/dev/Downloads/input (5).txt', 'r') as f:
  lines = f.readlines()

packet = lines[0]
for i in range(0,len(packet)-4):
    subp = packet[i:(i+4)]
    if len(list(set(subp)))==4:
        print(subp)
        print(i)
        break


for i in range(0,len(packet)-14):
    subp = packet[i:(i+14)]
    if len(list(set(subp)))==14:
        print(subp)
        print(i)
        break