import sys
INPUT_PATH = sys.argv[1] if len(sys.argv) > 1 else "input.txt"



with open(INPUT_PATH, 'r') as f:
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