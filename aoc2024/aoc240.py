import sys
INPUT_PATH = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

s1 = 0
s2 = 0

prod = True

if prod:
    with open(INPUT_PATH, 'r') as f:
        lines = f.readlines()
else:
    lines = """""".split("""
""")

for line in lines:
    print(line)
print(s1)
print(s2)