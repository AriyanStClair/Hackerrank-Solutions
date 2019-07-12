from sys import stdin 
n = int(input()) # number of elements in the set
s = set(map(int, input().split())) 
N = int(input()) # number of commands
commands = stdin.read().splitlines() # store commands in array

for command in commands: # iterate through list of commands
    command = command.split(' ') # split commands by whitespace
    if command[0] == 'pop':
            s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))
