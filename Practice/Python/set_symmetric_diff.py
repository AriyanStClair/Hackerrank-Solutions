# get input
e = int(input())
english = set(map(int,input().split()))
f = int(input())
french = set(map(int,input().split()))

result = len(english.symmetric_difference(french))
print(result)
