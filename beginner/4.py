#!/bin/python3
#problem link  https://www.hackerrank.com/challenges/plus-minus/problem
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    nz=0
    np=0
    nn=0
    res=[]
    for i in arr:
        if i==0:
            nz+=1
        elif i<0:
            nn+=1
        elif i>0:
            np+=1
    x=np/len(arr)
    y=nn/len(arr)
    z=nz/len(arr)
    res.append(x)
    res.append(y)
    res.append(z)
    return res