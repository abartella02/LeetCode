#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'finalState' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_INTEGER_ARRAY operations as parameter.
#


def finalState(operations):
    listToBin = lambda x: int("".join(map(str, x)), 2)
    l = 0b0

    if not operations:
        return 0
    length = max(max(i) for i in operations)
    for op in operations:
        base = [0 for _ in range(length + 1)]
        if not (op[0] == 0 or op[1] == 0):
            if op[0] == op[1]:
                base[op[0] - 1] = 1
            else:
                base[op[0] - 1 : op[1]] = [1] * (op[1] - op[0] + 1)
        l = l ^ listToBin(base)

    l = "{:07b}".format(l)
    total = 0
    for idx, num in enumerate(l):
        if int(num):
            total += idx + 1

    return total


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    operations_rows = int(input().strip())
    operations_columns = int(input().strip())

    operations = []

    for _ in range(operations_rows):
        operations.append(list(map(int, input().rstrip().split())))

    result = finalState(operations)

    fptr.write(str(result) + "\n")

    fptr.close()

"""
STDIN    Function
-----    --------
3     →  operations[] size q = 3
2     →  operations[i][] size = 2 (always)
3 4   →  operations = [[3, 4], [2, 3], [2, 2]]
2 3
2 2

STDOUT
-----
4
"""
