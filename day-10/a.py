with open("data.txt", "r") as f:
    data = [string.strip() for string in f]

starts = [(y, xI) for y, line in enumerate(data) for xI, char in enumerate(line) if char == "0"]
result = 0

directions = ((1,0), (-1,0), (0,1), (0,-1))
def findTrail(y, x, number, visited):
    global result, data, directions
    
    for direction in directions:
        tempY, tempX = y + direction[0], x + direction[1]
        if 0 <= tempY < len(data) and 0 <= tempX < len(data[0]):
            if  data[tempY][tempX] == str(number) and (tempY,tempX):
                if number == 9 and (tempY,tempX) not in visited:
                    result += 1
                    visited.append((tempY,tempX))
                    findTrail(y, x, number, visited)
                    break
                findTrail(tempY, tempX, number + 1, visited)

for index, (y, x) in enumerate(starts):
    findTrail(y, x, 1, [])
    #print(f"{index + 1} -> {result}")

print(result)