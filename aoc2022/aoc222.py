# a rock b paper c scissors
# x rock y paper z scissors
orda = ord('A')
ordx = ord('X')


def match(p):
    p1 = p[0]
    p2 = p[1][0]
    print(p1)
    print(p2)
    scores = [0, 0]
    scores[0] += ord(p1) - orda + 1
    scores[1] += ord(p2) - ordx + 1
    if scores[0] == scores[1]:
        scores[0] += 3
        scores[1] += 3
    elif scores[0] == 1 and scores[1] == 2:
        scores[1] += 6
    elif scores[0] == 1 and scores[1] == 3:
        scores[0] += 6
    elif scores[0] == 2 and scores[1] == 1:
        scores[0] += 6
    elif scores[0] == 2 and scores[1] == 3:
        scores[1] += 6
    elif scores[0] == 3 and scores[1] == 1:
        scores[1]+=6
    elif scores[0] == 3 and scores[1] == 2:
        scores[0] += 6
    return scores


def match2(p):
    p1 = p[0]
    p2 = p[1][0]
    # scores = [0, 0]
    # scores[0] += ord(p1) - orda + 1
    if p1 == 'A' and p2 == 'X':
        scores = [7,3]
    if p1 == 'A' and p2 == 'Y':
        scores = [4,4]
    if p1 == 'A' and p2 == 'Z':
        scores = [1,8]
    if p1 == 'B' and p2 == 'X':
        scores = [8,1]
    if p1 == 'B' and p2 == 'Y':
        scores = [5,5]
    if p1 == 'B' and p2 == 'Z':
        scores = [2,9]
    if p1 == 'C' and p2 == 'X':
        scores = [9,2]
    if p1 == 'C' and p2 == 'Y':
        scores = [6,6]
    if p1 == 'C' and p2 == 'Z':
        scores = [3,7]
    return scores

s1 = 0
s2 = 0
with open('/Users/dev/Downloads/input (1).txt', 'r') as f:
    for line in f:
        if line.strip():  # Skip blank lines.
            scores = match(line.split(' '))
            s1 += scores[0]
            s2 += scores[1]
print(s1)
print(s2)
