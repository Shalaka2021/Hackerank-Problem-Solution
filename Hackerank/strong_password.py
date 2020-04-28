#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    #if(n<6):
    #    return 6-n;
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    cnt_sc=0;
    cnt_dg=0;
    cnt_lc=0;
    cnt_uc=0;

    for i in password:
        if(i in numbers):
            cnt_dg+=1;
        if(i in lower_case):
            cnt_lc+=1;
        if(i in upper_case):
            cnt_uc+=1;
        if(i in special_characters):
            cnt_sc+=1;

    cnt=0;
    if(cnt_dg==0):
        cnt+=1;
    if(cnt_lc==0):
        cnt+=1;
    if(cnt_uc==0):
        cnt+=1;
    if(cnt_sc==0):
        cnt+=1;
    
    #print(cnt);

    if(n<6 and cnt<(6-n)):
        return 6-n;
    return cnt;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
