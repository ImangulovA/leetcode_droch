from itertools import accumulate, filterfalse
def bus(arr):
    res = []
    all_s = list(accumulate(arr))
    max_s = all_s[-1]
    for s in all_s:
        q, r = divmod(max_s, s)
        if r == 0 and len(set(filterfalse(lambda x: x%s, all_s))) == q:
            res.append(s)
    return res


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = bus(a)
    print(' '.join(map(str, result)))