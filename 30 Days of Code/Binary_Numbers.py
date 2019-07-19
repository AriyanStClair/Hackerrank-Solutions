#!/bin/python3

import math
import os
import random
import re
import sys

#


if __name__ == '__main__':
    n = int(input())
    binary = str(bin(n))[2:] # remove 0b from conversion
    count = 0
    consecutive = []
    
    for bit in binary:
        if bit == '1':
            count +=1
            consecutive.append(count) # append count to get number of consecutive 1s
        else:
            count = 0
    print(max(consecutive)) # find maximum number of consecutive 1s
  
