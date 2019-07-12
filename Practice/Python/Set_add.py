# Find out how many distinct countries are inputted

n = int(input()) # how many elements to add to set
s = set()         
for i in range(n):
    s.add(input())
print(len(s)) # the length of s is the number of distinct countries
