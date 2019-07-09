def count_substring(string, sub_string):
    n = len(sub_string)
    count = 0
    # checks every substring of string of the same length of sub_string
    for i in range(0,len(string)):
        sub = string[i:i+n] 
        if sub == sub_string:
            count = count + 1
    return count
    
    if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
