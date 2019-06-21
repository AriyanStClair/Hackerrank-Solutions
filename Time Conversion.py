#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.split(':')  
    if s[-2:] == 'PM': # checks if AM or PM
         if time[0] != '12': 
            time[0] = str(int(time[0]) + 12) # performing conversion
    else:
        if time[0] == '12': 
            time[0] = '00'
    result = ':'.join(time)
    return result[:-2]
   

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
