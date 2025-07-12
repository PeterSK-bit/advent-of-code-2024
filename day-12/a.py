with open("data.txt", "r") as f:
    data = [line.strip() for line in f]

answer = 0

directions = ((1,0),(0,1),(-1,0),(0,-1))
def mapArea(y:int, x:int, plant:str, visited:list, counted:list = []):
    global answer, fanceCounter, visitedCounter
    for dy, dx in directions:
        currentX, currentY = x+dx, y+dy
        if 0 <= currentY < len(data) and 0 <= currentX < len(data[0]) and data[currentY][currentX] == plant:
            if (currentY, currentX) not in visited:
                visited.append((currentY, currentX))
                visitedCounter += 1
                mapArea(currentY, currentX, plant, visited, counted)
        elif (currentY, currentX, dy, dx) not in counted:
            fanceCounter += 1
            counted.append((currentY, currentX, dy, dx))

visited = []

for y, line in enumerate(data):
    for x, plant in enumerate(line):
        if (y,x) not in visited:
            fanceCounter = 0
            visitedCounter = 0
            mapArea(y, x, plant, visited)
            visitedCounter = 1 if not visitedCounter else visitedCounter
            answer += fanceCounter*visitedCounter

print(answer)