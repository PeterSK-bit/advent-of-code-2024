with open("data.txt") as f:
    museum = [string.strip() for string in f]
del f

directions = [(1,0), (0,1), (-1,0), (0,-1)]
directionI = 3

for i,line in enumerate(museum):
    if line.find("^") != -1:
        position = [line.find("^"),i]

nextX, nextY = position
print(museum[nextY][nextX])

while nextX in range(0, len(museum[0])) and nextY in range(0,len(museum)):
    

    if museum[nextY][nextX] == "#":
        directionI = (directionI + 1) % 4
    else:
        museum[nextY] = museum[nextY][:nextX] + "x" + museum[nextY][nextX+1:]
        position[0] = nextX
        position[1] = nextY
    
    nextX = position[0] + directions[directionI][0]
    nextY = position[1] + directions[directionI][1]

result = 0
for line in museum:
    result += line.count("x")
print(result)