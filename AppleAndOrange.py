#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c=0
    cb=0
    for i in range(len(apples)):
        if((apples[i]+a)>=s and (apples[i]+a)<=t):
            c+=1
    for i in range(len(oranges)):
        if((oranges[i]+b)<=t and (oranges[i]+b)>=s):
            cb+=1
    
    print(c)
    print(cb)
            

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
