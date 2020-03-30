#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    arr=[];
    brr=[];
    for i in range(len(a)):
        if(a[i] in arr):
            print(a);
            print(a[i]);
            print(arr);
            print(brr);
            dist=abs(i-arr.index(a[i]));
            print(dist);
            brr.append(dist);
        arr.append(a[i]);

    if(len(brr)!=0):
        minn=min(brr);
    else:
        minn=-1;

    print(minn);

    return minn;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
