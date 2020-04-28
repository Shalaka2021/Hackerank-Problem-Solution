#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alpha="qwertyuiopasdfghjklzxcvbnm";

    alpha=list(alpha);

    alpha.sort();

    print(alpha);
    print(len(alpha));

    arr=[];

    for i in word:
        ind=alpha.index(i);
        arr.append(h[ind]);

    maxx=max(arr);

    ans=maxx*len(word);

    return ans;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
