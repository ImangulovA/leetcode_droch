import sys
INPUT_PATH = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

calories = []
nn = 0
with open(INPUT_PATH, 'r') as f:
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