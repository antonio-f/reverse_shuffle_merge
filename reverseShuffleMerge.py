#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import Counter

def reverseShuffleMerge(s):
    m = Counter(s)
    r = {c: int(n / 2) for c, n in m.items()}
    sh = {c: int(n / 2) for c, n in m.items()}
    l = []
    for c in reversed(s):
        if r[c] > 0:
            while l and l[-1] > c and sh[l[-1]] > 0:
                removed = l.pop()
                r[removed] += 1
                sh[removed] -= 1
            l.append(c)
            r[c] -= 1
        else:
            sh[c] -= 1

    return ''.join(l)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
