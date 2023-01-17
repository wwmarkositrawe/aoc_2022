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
        result += scissors + isLost
    elif elem == 'AY':
        result += rock + isDraw
    elif elem == 'AZ':
        result += paper + isWinner
    elif elem == 'BX':
        result += rock + isLost
    elif elem == 'BY':
        result += paper + isDraw
    elif elem == 'BZ':
        result += scissors + isWinner
    elif elem == 'CX':
        result += paper + isLost
    elif elem == 'CY':
        result += scissors + isDraw
    elif elem == 'CZ':
        result += rock + isWinner
        
print(result)

