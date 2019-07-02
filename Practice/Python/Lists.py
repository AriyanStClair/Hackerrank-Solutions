from sys import stdin 
if __name__ == '__main__':
    N = int(input())
    commands = stdin.read().splitlines() # store commands in array
    arr = [] # initialize array

    for command in commands: # iterate through list of commands
        command = command.split(' ') # split commands by whitespace
        if command[0] == 'insert':
            arr.insert(int(command[1]),int(command[2]))
        elif command[0] == 'remove':
            arr.remove(int(command[1]))
        elif command[0] == 'append':
            arr.append(int(command[1]))
        elif command[0] == 'print':
            print(arr)
        elif command[0] == 'reverse':
            arr.reverse()
        elif command[0] == 'pop':
            arr.pop()
        elif command[0] == 'sort':
            arr.sort()

