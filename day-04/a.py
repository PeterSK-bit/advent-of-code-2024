import re

with open("data.txt") as f:
    data = list(map(lambda x: x.strip() ,f.readlines()))
del f

result = 0
#horizontal, correct
for line in data:
    result += len(re.findall("XMAS", line)) + len(re.findall("SAMX", line))

#diagonal und vertical
for y in range(len(data)-3):
    for x in range(len(data[0])):
    #vertical
        verticalStr = data[y][x] + data[y+1][x] + data[y+2][x] + data[y+3][x]
        if verticalStr == "XMAS" or verticalStr == "SAMX":
            result += 1
    #diagonal -> left to right
        if len(data[0]) - 3 > x:
            diagonalStr = data[y][x] + data[y+1][x+1] + data[y+2][x+2] + data[y+3][x+3]
            if diagonalStr == "XMAS" or diagonalStr == "SAMX":
                result += 1
    # diagonal <- right to left
        if x > 2:
            diagonalStr = data[y][x] + data[y+1][x-1] + data[y+2][x-2] + data[y+3][x-3]
            if diagonalStr == "XMAS" or diagonalStr == "SAMX":
                result += 1
print(result) #desire output -> 18