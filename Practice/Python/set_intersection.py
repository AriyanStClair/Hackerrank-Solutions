#The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, 
#some have subscribed only to French, and some have subscribed to both newspapers.

#You are given two sets of student roll numbers. 
#One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
#Your task is to find the total number of students who have subscribed to both newspapers.


# Get input
e = int(input()) # number of students that subscribed to english paper
english = set(map(int,input().split())) # roll numbers of english subscribers
f = int(input()) # number of students that subscribed to french paper
french = set(map(int,input().split())) # roll numbers of french subscribers

intersection = len(english.intersection(french)) # number of students subscribed to both
print(intersection)
