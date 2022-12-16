rucksum = 0
with open('/Users/dev/Downloads/input (2).txt', 'r') as f:
  for line in f:
    if line.strip():  # Skip blank lines.
      firsth = line[:(len(line)//2)]
      secondh = line[(len(line)//2):]
      common = list(set(firsth).intersection(secondh))
      if (common[0] >= 'a') & (common[0] <= 'z'):
        rucksum += ord(common[0]) - ord('a') + 1
      else:
        rucksum += ord(common[0]) - ord('A') + 27
      # print(rucksum)

with open('/Users/dev/Downloads/input (2).txt', 'r') as f:
  lines = f.readlines()

rucksum2 = 0
for i in range(0,len(lines),3):
    l1 = lines[i][:-1]
    l2 = lines[i+1][:-1]
    l3 = lines[i+2][:-1]

    common = list(set(l1).intersection(l2).intersection(l3))
    print(common)
    if (common[0] >= 'a') & (common[0] <= 'z'):
      rucksum2 += ord(common[0]) - ord('a') + 1
    else:
      rucksum2 += ord(common[0]) - ord('A') + 27
    print(rucksum2)
