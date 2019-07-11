import textwrap
from collections import OrderedDict

def merge_the_tools(string, k):
    letter = []
    string = textwrap.wrap(string, width = k) # split string into parts of length k
    for substring in string:
        substring = "".join(OrderedDict.fromkeys(substring)) # remove repeated string
        letter.append(substring)
    print(*letter,sep = '\n')


       

   

    


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
