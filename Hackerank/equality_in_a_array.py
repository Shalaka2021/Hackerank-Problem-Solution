#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    set1=set(arr);
    list1=list(set1);

    brr=[];
    for i in list1:
        n=arr.count(i);
        brr.append(n);

    maxx=max(brr);

    ans=len(arr)-maxx;

    print(ans);

    return ans;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
