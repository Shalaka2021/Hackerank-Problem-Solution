#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):

    s_len=len(s);
    t_len=len(t);
    """if(s_len<t_len):
        return "No";"""

    cnt=0;

    s=list(s);
    t=list(t);

    if(s_len>=t_len):
        for i in range(t_len):
            if(s[i]!=t[i]):
                break;
        l=s_len-i;
        for _ in range(l):
            s.pop();
            cnt+=1;

        for j in range(i,t_len):
            s.append(t[j]);
            cnt+=1;
    else:
        flag=1;
        for i in range(s_len):
            if(s[i]!=t[i]):
                break;
        #i=i+1;
        diff=t_len-i-1;
        print(diff,i);
        if((diff%2==0 and k%2==0) or (diff%2!=0 and k%2!=0)):
            return "Yes";
        return "No";

    flag=1;    

    for i in range(len(s)):
        if(s[i]!=t[i]):
            flag=0;
            break;
    if(flag==1 and cnt<=k):
        return "Yes";
    return "No";

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
