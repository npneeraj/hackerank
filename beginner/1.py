#!/bin/python3
#problem link  https://www.hackerrank.com/challenges/compare-the-triplets/problem

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    sa=0
    sb=0
    l=[]
    for i in range(3):
        if a[i]<b[i]:
            sb+=1
        elif a[i]>b[i]:
            sa+=1
    l.append(sa)
    l.append(sb)
    return l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
