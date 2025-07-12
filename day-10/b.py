with open("data.txt", "r") as f:
    data = [string.strip() for string in f]

starts = [(y, xI) for y, line in enumerate(data) for xI, char in enumerate(line) if char == "0"]
result = 0
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

def findTrail(y, x, number, path):
    global result, data, directions
    
    path.append((y, x))
    for direction in directions:
        tempY, tempX = y + direction[0], x + direction[1]
        
        if 0 <= tempY < len(data) and 0 <= tempX < len(data[0]):
            if data[tempY][tempX] == str(number) and (tempY, tempX) not in path:
                if number == 9:
                    result += 1
                else:
                    findTrail(tempY, tempX, number + 1, path[:])

for y, x in starts:
    findTrail(y, x, 1, [])

print(result)
