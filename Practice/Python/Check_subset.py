# Task: Check if A is a Subset of B
# get input
n = int(input()) # number of test cases(inputs)

for i in range(n):
    num_A = int(input()) # number of elements in set A
    A = set(map(int, input().split())) 
    num_B = int(input()) # number of elements in set B
    B = set(map(int, input().split())) 

    if len(A.intersection(B)) == num_A: # A is a subset of B if all elements of A is in B
        print("True")
    else:
        print("False")
