#!/bin/python3
#problem link https://www.hackerrank.com/challenges/diagonal-difference/problem
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sr=0
    sl=0
    l=[]
    j=len(arr)-1
    for i in range(len(arr)):
        sl=sl+arr[i][i]
        #l.append(arr[i][j])
        sr=sr+arr[i][j]
        j=j-1
           
    return abs(sl-sr)   
    #return sl,sr
    #return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()