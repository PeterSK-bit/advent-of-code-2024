# --CORRECT-- #
def widenField(field):
    new_field = []
    for row in field:
        new_row = []
        for char in row:
            if char == ".":   new_row.extend([".","."])
            elif char == "#": new_row.extend(["#","#"])
            elif char == "@": new_row.extend(["@","."])
            elif char == "O": new_row.extend(["[","]"])
        new_field.append(new_row)
    return new_field

# --CORRECT-- #
def moveBox(x:int, y:int, dx:int, dy:int) -> bool:
    lx, ly, rx, ry = (x, y, x+1, y) if field[y][x] == "[" else (x-1, y, x, y)
    
    if field[ly+dy][lx+dx] != "#" and field[ry+dy][rx+dx] != "#":
        if field[ly+dy][lx+dx] in "[]" and dx == 0:
            if not moveBox(lx+dx, ly+dy, dx, dy): return False

        if field[ry+dy][rx+dx] in "[]" and dx == 0:
            if not moveBox(rx+dx, ry+dy, dx, dy): return False

        field[ly+dy][lx+dx] = "["
        if field[ly][lx] != "]": field[ly][lx] = "."
        field[ry+dy][rx+dx] = "]"
        if field[ry][rx] != "[": field[ry][rx] = "."

        return True
    return False

# data loading and formating
# --CORRECT-- #
with open("data.txt","r") as f:
    field = []
    for line in f:
        if line == "\n": break
        field.append(str(line.strip()))
    commands = "".join(line.strip() for line in f)

directions = { # X, Y
    "<": (-1, 0),
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1)
}

field = widenField(field)

# finding start position 
# --CORRECT-- #
def findStart(field) -> tuple[int, int]:
    for ly, line in enumerate(field):
        for lx, char in enumerate(line):
            if char == "@":
                return lx, ly

x, y = findStart(field)
field[y][x] = "."

# all 20_000 commands running
for command in commands:
    dx, dy = directions[command]
    nx, ny = x + dx, y + dy

    if field[ny][nx] == ".":
        x, y = nx, ny
    elif field[ny][nx] in "[]":
        if moveBox(nx, ny, dx, dy):
            x, y = nx, ny

result = 0
for y, line in enumerate(field):
    for x, char in enumerate(line):
        if char == "[":
            result += x + y * 100
print(result)

# ALL TEST CASE CORRECT

# too low: 
# 1_528_292
# 1_534_812 (answer after error in data formating | len(commands) => 0)

# wrong answer:
# 1_595_021

# PROBABLY CORRECT ANS 1_538_862