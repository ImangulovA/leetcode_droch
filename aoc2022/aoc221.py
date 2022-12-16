calories = []
nn = 0
with open('/Users/dev/Downloads/input.txt', 'r') as f:
  for line in f:
    if line.strip():  # Skip blank lines.
      nn += int(line)
    else:
      calories.append(nn)
      nn = 0
calories.append(nn)
nn = 0

print(max(calories))
calories.sort()
print(sum(calories[-3::]))