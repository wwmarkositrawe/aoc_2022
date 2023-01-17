input_data = open("Day2\data.txt").read().rstrip().split("\n")

li = [x.replace(' ', '') for x in input_data]

result = 0

isLost = 0
isDraw = 3
isWinner = 6

rock = 1
paper = 2
scissors = 3

for elem in li:
    if elem == 'AX':
        result += rock + isDraw
    elif elem == 'AY':
        result += paper + isWinner
    elif elem == 'AZ':
        result += scissors + isLost
    elif elem == 'BX':
        result += rock + isLost
    elif elem == 'BY':
        result += paper + isDraw
    elif elem == 'BZ':
        result += scissors + isWinner
    elif elem == 'CX':
        result += rock + isWinner
    elif elem == 'CY':
        result += paper + isLost
    elif elem == 'CZ':
        result += scissors + isDraw
        
print(result)

