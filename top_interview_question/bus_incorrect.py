#!/bin/python3

import os
import sys
from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def check_sit(a, n, p):
    iterator = 0
    while iterator < n:
        currentsum = a[iterator]
        while currentsum < p:
            try:
                iterator += 1
                currentsum += a[iterator]
            except:
                return False
        if currentsum > p:
            return False
        iterator += 1
    return True


# Complete the solve function below.
def solve(a, n):
    suma = sum(a)
    maxa = max(a)
    cumsums = [a[0]]
    for i in range(1, n):
        cumsums.append(cumsums[-1] + a[i])
    factorsa = factors(suma)

    possible_answers = list(set(factorsa).intersection(cumsums))
    del factorsa, cumsums
    possible_answers = [i for i in possible_answers if i >= maxa]

    for p in possible_answers:
        if check_sit(a, n, p) == False:
            possible_answers.remove(p)
    return sorted(possible_answers)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a, a_count)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
