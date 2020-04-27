#!/bin/python3
#problem link  https://www.hackerrank.com/challenges/staircase/problem
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        #for j in range(i):
        spaces=n-i
        print(spaces*' ',end='')
        print(i*'#')
        #print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)