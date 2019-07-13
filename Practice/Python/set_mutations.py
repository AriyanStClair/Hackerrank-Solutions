#You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set .

#Your task is to execute those operations and print the sum of elements from set .


# get input

num_A = int(input()) # num of elements of set A
A = set(map(int, input().split()))
set_num = int(input()) # number of other sets 

for i in range(set_num): 
    (operation, n) = input().split()
    other_set = set(map(int, input().split()))
    
    if operation == 'update':
        A.update(other_set)

    elif operation == 'intersection_update':
        A.intersection_update(other_set)

    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)

    elif operation == 'difference_update':
        A.difference_update(other_set)

print(sum(A))
    
