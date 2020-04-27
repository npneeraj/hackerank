#!/bin/python3
#problem link   https://www.hackerrank.com/challenges/birthday-cake-candles/problem
import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    temp=sorted(ar)
    max=temp[-1]
    c=0
    for i in temp:
        if i==max:
            c+=1
    
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
