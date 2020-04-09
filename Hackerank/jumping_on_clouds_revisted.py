

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    cnt_thunder=0;
    tot=0;

    flag=0;
    len_c=len(c);
    i=k%len_c;
    while(i!=0 ):
        #print("hello");
        flag=1;
        tot+=1;
        #print(i,"--",c[i]);
        if(c[i]==1):
            cnt_thunder+=1;
            print(cnt_thunder);
        i=(i+k)%len_c;

    if(c[0]==1):
        x=3;
    else:
        x=1;
    ans=100-tot-(cnt_thunder*2)-x;

    #print(ans);

    return ans;
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
