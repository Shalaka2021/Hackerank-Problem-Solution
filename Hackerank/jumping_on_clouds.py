#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    c_len=len(c);

    i=0;
    cnt=0;
    
    while(i!=(c_len-1)):
        cnt+=1;
        print("i--",i," cnt--",cnt);
        print(i!=c_len-2);
        if(i!=c_len-2 and c[i+2]==0):
            i=i+2;
        else:
            i=i+1;

    print(cnt);

    return cnt;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
