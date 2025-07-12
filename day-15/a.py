with open("data.txt","r") as f:
    field = []
    for line in f:
        if line == "\n":  
            break
        field.append(list(line.strip()))


    commands = [line.strip() for line in f]

directions = { #X, Y
    "<": (-1, 0),
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1)
}

width = len(field[0])
height = len(field)
# 0 <= x+dx < width and 0 <= y+dy < height

for ly, line in enumerate(field):
    for lx, char in enumerate(line):
        if char == "@":
            x, y = lx, ly
            break

field[y][x] = "."

for line in commands:
    for command in line:
        dx, dy = directions[command]
        nx, ny = x + dx, y + dy

        if field[ny][nx] == ".":
            x, y = nx, ny
        elif field[ny][nx] == "O":
            length = 0
            while field[ny + dy * length][nx + dx * length] == "O":
                length += 1
            bx, by = nx + dx * length, ny + dy * length
            if field[by][bx] == ".":
                field[by][bx] = "O"
                field[ny][nx] = "."
                x, y = nx, ny

result = 0
for y, line in enumerate(field):
    for x, char in enumerate(line):
        #print(char, end="")
        if char == "O":
            result += x+y*100
    #print()
print(result)  