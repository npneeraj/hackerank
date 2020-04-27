#!/bin/python3
#problem link   https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    temp=sorted(arr)
    min=sum(temp[:-1])
    max=sum(temp[1:])

    return min,max
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    min,max=miniMaxSum(arr)
    print(min,max)