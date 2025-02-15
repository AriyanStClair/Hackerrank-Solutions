#Task

You are given a string S. 
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, 
# digits, lowercase and uppercase characters.

#Input Format

#A single line containing a string S.

#Output Format

#In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
#In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
#In the third line, print True if S has any digits. Otherwise, print False. 
#In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
#In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    string = input()
    print(any(char.isalnum() for char in string))
    print(any(char.isalpha()for char in string))
    print(any(char.isdigit()for char in string))
    print(any(char.islower()for char in string))
    print(any(char.isupper()for char in string))
