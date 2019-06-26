#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s = list(s) # list of characters in string
    count = counter(s) # count of a in s

    repeats = n//len(s) # lets know how many complete repeats occurs

    if s == 'a': # if the input string is only a
        return repeats

    else:
        remainder = n - (repeats * len(s)) # find how many letters are left
        leftover = s[:remainder] # save portion of s that is left
        count_leftover = counter(leftover) # count of a in leftover
        count = (count * repeats) + count_leftover # final count
        return count

def counter(s): # counter that counts how many a in list
    count = 0 
    for i in range(len(s)):
        if s[i] == 'a':
            count = count + 1
    return count

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
