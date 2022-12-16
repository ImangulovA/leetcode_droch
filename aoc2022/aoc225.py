

with open('/Users/dev/Downloads/input (4).txt', 'r') as f:
  lines = f.readlines()


cargos = lines[:8]
commands = lines[10:]
n = 9
stacks = [[] for i in range(9)]
for l in cargos:
    if '1' not in l:
        s = list((l[k:k+3] for k in range(0,36,4)))
        for j in range(9):
            if '[' in s[j]:
                stacks[j].append(s[j])
# p1
# for c in commands:
#     instr = list(map(int, c.replace('\n', '').split()[1::2]))
#     for i in range(instr[0]):
#         transpcargo = stacks[instr[1]-1].pop(0)
#         stacks[instr[2]-1] = [transpcargo, *stacks[instr[2]-1]]

# p2

for c in commands:
    instr = list(map(int, c.replace('\n', '').split()[1::2]))
    transpcargo = stacks[instr[1]-1][:instr[0]]
    stacks[instr[1] - 1] = stacks[instr[1]-1][instr[0]:]
    stacks[instr[2]-1] = [*transpcargo, *stacks[instr[2]-1]]
answer = ''
for s in stacks:
    answer += s[0]

print(answer.replace('[','').replace(']',''))