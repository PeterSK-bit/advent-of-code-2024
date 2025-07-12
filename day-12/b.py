with open("data.txt", "r") as f:
    data = [line.strip() for line in f]

answer = 0

def mapArea(y:int, x:int, plant:str):
    global answer, visitedCounter, counted, visited
    for dy, dx in ((1,0),(0,1),(-1,0),(0,-1)):
        currentX, currentY = x+dx, y+dy
        if 0 <= currentY < len(data) and 0 <= currentX < len(data[0]) and data[currentY][currentX] == plant:
            if (currentY, currentX) not in visited:
                visited.append((currentY, currentX))
                visitedCounter += 1
                mapArea(currentY, currentX, plant)
        elif (currentY, currentX, dy, dx) not in counted:
            counted.append((currentY, currentX, dy, dx))

def IDontKnowHowToNameThisShit(y, x, dy, dx):
    counted.remove((y, x, dy, dx))
    for yIncrement, xIncrement in ((1,0),(0,1),(-1,0),(0,-1)):
        if (y+yIncrement, x+xIncrement, dy, dx) in counted:
            IDontKnowHowToNameThisShit(y+yIncrement, x+xIncrement, dy, dx)

visited = []
for y, line in enumerate(data):
    for x, plant in enumerate(line):
        if (y,x) not in visited:
            visited.append((y, x))
            visitedCounter = 1
            counted = []
            edges = 0
            mapArea(y, x, plant)
            while counted:
                IDontKnowHowToNameThisShit(*counted[0])
                edges += 1
            answer += visitedCounter*edges
print(answer)