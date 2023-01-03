#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    kk,vv= 0,0
    res = 0

    set(arr)
    fe = { i : 0 for i in arr }
    
    for bird in arr:
        for Key in fe.keys():
            if Key == bird:
                fe[Key] += 1
    
    for k,v in fe.items():
        if v == vv:
            if k < kk:
                res = k
                vv,kk = v,k
        elif v > vv:
            res = k
            vv,kk = v,k
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
