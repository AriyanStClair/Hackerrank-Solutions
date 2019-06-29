from sys import stdin 
n = int(input())
phoneBook = dict()

for i in range(n): # read n inputs and store in phoneBook dictionary
    contact_info = input()
    name, phoneNumber = contact_info.split(" ")
    phoneBook[name] = phoneNumber
    
queries = stdin.read().splitlines() 

for name in queries: # check for name in queries
    if name not in phoneBook: # if name is not in phoneBook
        print('Not found')
    else:
        print(name + '=' + phoneBook[name])
