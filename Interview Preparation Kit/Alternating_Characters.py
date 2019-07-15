#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    for char in s:
        if s.count(char) == len(s): # if all of the letters ae the same delete length - 1
            return(len(s)- 1)
        else:
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    count +=1
            return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
