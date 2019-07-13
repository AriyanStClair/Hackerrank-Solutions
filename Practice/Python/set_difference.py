# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

#You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
# and the other set is subscribed to the French newspaper. 
# The same student could be in both sets.  Your task is to find the total number of students who have subscribed to only English newspapers.

# Get input
e = int(input()) # number of students that subscribed to english paper
english = set(map(int,input().split())) # roll numbers of english subscribers
f = int(input()) # number of students that subscribed to french paper
french = set(map(int,input().split())) # roll numbers of french subscribers

english_only = len(english.difference(french)) # english only subscribers
print(english_only)
