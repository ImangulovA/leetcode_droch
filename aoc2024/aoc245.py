s1 = 0
s2 = 0

prod = True

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_5.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split("""
""")


def topological_sort_dfs(graph, nodes):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor in nodes:
                    dfs(neighbor)
        stack.append(node)

    for node in nodes:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse the stack for topological order


# Usage


dictpage = {}
for line in lines:
    if '|' in line:
        nums = list(map(int, line.split('|')))
        if nums[0] in dictpage:
            dictpage[nums[0]].append(nums[1])
        else:
            dictpage[nums[0]] = [nums[1]]
    else:
        if ',' in line:
            order = list(map(int, line.split(',')))
            correct = True
            for i in range(1,len(order)):
                if order[i-1] not in dictpage:
                    correct = False
                else:
                    if order[i] not in dictpage[order[i-1]]:
                        correct = False
            if correct:
                # print(order)
                # print(order[len(order)//2])
                s1 += order[len(order)//2]
            else:
                new_order = topological_sort_dfs(dictpage, order)
                print(len(order), len(new_order), order,new_order)
                s2 += new_order[len(new_order)//2]

print(s1)
print(s2)
