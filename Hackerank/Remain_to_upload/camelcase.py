#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    cnt=1;
    for i in s:
        if(i==i.upper()):
            cnt+=1;

    print(cnt);

    return cnt;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
