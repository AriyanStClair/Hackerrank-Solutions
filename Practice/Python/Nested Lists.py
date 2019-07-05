
def second_lowest(numbers): # finds second_lowest number
    lowest = min(numbers) 
    length = len(numbers)
    i = 0
    while(i<length):
        if numbers[i] == lowest:
            numbers.remove(numbers[i])
            length = length - 1
            continue 
        i = i + 1
    return min(numbers)

if __name__ == '__main__':
    
    gradebook = [] # store name and score
    scores = [] # store scores
    second_lowest_names = [] # store names of second lowest
    for _ in range(int(input())):
        name = input()
        score = float(input())
        gradebook.append([name,score])
        scores.append(score)
    # get min of entire list, remove from list, get the min of that sublist
    
    second_lowest = second_lowest(scores)
    
    for i in range(0,len(gradebook)):
        if gradebook[i][1] == second_lowest: # get names
            second_lowest_names.append(gradebook[i][0])
        second_lowest_names.sort() # sort second _lowest
    print(*second_lowest_names, sep = "\n")  # print

    
