#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import cycle;

# Complete the repeatedString function below.
def repeatedString(s, n):
    if(len(s)==1 and s[0]=='a'):
        return n;

    cnt=0;
    if(n<=len(s)):
        for i in range(len(s)):
            if(i<n and s[i]=='a'):
                cnt+=1;

        return cnt;

    s_len=len(s);
    tot=0;
    for i in s:
        if(i=='a'):
            tot+=1;

    qou=n//s_len;

    cnt=tot*qou;

    rem=n%s_len;
    
    for i in range(rem):
        if(s[i]=='a'):
            cnt+=1;
    

    print(cnt);

    return cnt;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
