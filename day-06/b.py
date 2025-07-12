# runtime around 1min :)

with open("data.txt") as f:
    museum = [string.strip() for string in f]
del f

directions = [(1,0), (0,1), (-1,0), (0,-1)]
result = 0

temp = list(museum)
for lineI in range(len(museum)):
    for charI in range(len(museum[0])):
        if museum[lineI][charI] == "#":
            continue
        else:
            museum[lineI] = museum[lineI][:charI]+"#"+museum[lineI][charI+1:]

        for i,line in enumerate(museum):
            if line.find("^") != -1:
                position = [line.find("^"),i]

        nextX, nextY = position
        directionI = 3
        bumped_states = []

        while nextX in range(0, len(museum[0])) and nextY in range(0,len(museum)):
            if museum[nextY][nextX] == "#":
                if [position,directionI] in bumped_states:
                    result += 1
                    break
                bumped_states.append([list(position), directionI])
                directionI = (directionI + 1) % 4
            else:
                #museum[nextY] = museum[nextY][:nextX] + "x" + museum[nextY][nextX+1:]
                position[0] = nextX
                position[1] = nextY
            
            nextX = position[0] + directions[directionI][0]
            nextY = position[1] + directions[directionI][1]

        museum = list(temp)
print(result)