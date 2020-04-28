#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):

    for i in range(len(s)):
        print(s[i]);
    s=list(s);
    #s.sort();
    """for i in range(0,len(s)-1):
        print("world");
        print(i,i+1);
        print(s[i],s[i+1]);
        if(s[i]==s[i+1]):
            print("hello");
            #del s[i:i+2];
            s[i]=0;
            s[i+1]=0;"""
        
    """for i in range(0,len(s)-1):
        #print("world");
        print(i,i+1);
        print(s);
        #print(s[i],s[i+1],len(s));
        if(s[i]==s[i+1]):
            print("hello");
            del s[i];
            del s[i];
            i=-1;
            print(i);"""
    i=0;
    while(i<len(s)-1):
        try:
            print("world");
            print(i,i+1,"len-",len(s));
            print(s);
            #print(s[i],s[i+1],len(s));
            if(s[i]==s[i+1]):
                print("hello");
                del s[i];
                del s[i];
                i=0;
                print(i);
            else:
                i+=1;
        except Exception as a:
            pass;

    if(len(s)==0):
        return "Empty String";
    arr=str();
    for i in s:
        arr=arr+i;
    
    return (arr);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
