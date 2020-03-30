#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    cnt=0;
    set1=set(arr);
    list1=list(set1);
    list1.sort();
    for i in range(len(list1)):
        a=list1[i];
        if((a+d) in arr and (a+2*d) in arr):
            x=arr.count(a);
            y=arr.count(a+d);
            z=arr.count(a+2*d);
            cnt+=(x*y*z);
            print(x,y,z);

    print(cnt);

    return cnt;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
