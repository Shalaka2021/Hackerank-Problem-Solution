#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    cnt=0;

    m=str(n);
    print(m);
    
    m=list(m);
    print(m);
    
    for i in m:
        try:
            x=int(i);
            print(i);
            if(n%x==0):
                cnt+=1;
        except Exception as a:
            pass;
    
    print(cnt);
    
    return cnt;
            
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
