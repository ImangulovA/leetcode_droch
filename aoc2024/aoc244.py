s1 = 0
s2 = 0

prod = True

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_4.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("""
""")

for i in range(len(lines)):
    for k in range(len(lines[0])):
        if lines[i][k] == 'M':
            try:
                if lines[i][k+2] == 'M':
                    if lines[i+1][k+1] == 'A':
                        if lines[i+2][k] == 'S':
                            if lines[i+2][k+2] == 'S':
                                s2+=1
                                print(i,k,s2,'up')
            except:
                pass
        if lines[i][k] == 'M':
            try:
                if lines[i][k+2] == 'S':
                    if lines[i+1][k+1] == 'A':
                        if lines[i+2][k] == 'M':
                            if lines[i+2][k+2] == 'S':
                                s2+=1
                                print(i,k,s2,'right')
            except:
                pass
        if lines[i][k] == 'S':
            try:
                if lines[i][k+2] == 'S':
                    if lines[i+1][k+1] == 'A':
                        if lines[i+2][k] == 'M':
                            if lines[i+2][k+2] == 'M':
                                s2+=1
                                print(i,k,s2,'down')
            except:
                pass
        if lines[i][k] == 'S':
            try:
                if lines[i][k+2] == 'M':
                    if lines[i+1][k+1] == 'A':
                        if lines[i+2][k] == 'S':
                            if lines[i+2][k+2] == 'M':
                                s2+=1
                                print(i,k,s2,'left')
            except:
                pass
        if lines[i][k] == 'X':
            try:

                if lines[i][k+1] == 'M':
                    if lines[i][k+2] == 'A':
                        if lines[i][k+3] == 'S':
                            s1+=1
                            print(i,k,s1,'right')
            except:
                pass
            try:
                if lines[i+1][k+1] == 'M':
                    if lines[i+2][k+2] == 'A':
                        if lines[i+3][k+3] == 'S':
                            s1+=1
                            print(i,k,s1,'diashit')

            except:
                pass
            try:
                if i > 2:
                    if lines[i-1][k+1] == 'M':
                        if lines[i-2][k+2] == 'A':
                            if lines[i-3][k+3] == 'S':
                                s1+=1
                                print(i,k,s1,'diawhat')

            except:
                pass

            try:
                if k > 2:
                    if lines[i+1][k-1] == 'M':
                        if lines[i+2][k-2] == 'A':
                            if lines[i+3][k-3] == 'S':
                                s1+=1
                                print(i,k,s1,'diadown')
            except:
                pass
            try:
                if (i > 2) and (k > 2):
                    if lines[i-1][k-1] == 'M':
                        if lines[i-2][k-2] == 'A':
                            if lines[i-3][k-3] == 'S':
                                s1+=1
                                print(i,k,s1,'diaup')
            except:
                pass
            try:
                if k > 2 :
                    if lines[i][k-1] == 'M':
                        if lines[i][k-2] == 'A':
                            if lines[i][k-3] == 'S':
                                s1+=1
                                print(i,k,s1,'left')
            except:
                pass

            try:
                if lines[i+1][k] == 'M':
                    if lines[i+2][k] == 'A':
                        if lines[i+3][k] == 'S':
                            s1+=1
                            print(i,k,s1,'down')
            except:
                pass
            try:
                if i > 2 :
                    if lines[i-1][k] == 'M':
                        if lines[i-2][k] == 'A':
                            if lines[i-3][k] == 'S':
                                s1+=1
                                print(i,k,s1,'up')
            except:
                pass

print(s1)
print(s2)
