# well just observe it 

with open("data.txt", "r") as f:
    robots = []
    for line in f:
        pairs = line.strip().replace("p=", "").replace("v=", "").split(" ")
        for pair in pairs:
            x, y = map(int, pair.split(","))
            robots.append([x, y])

width = 101
height = 103
midX = width // 2
midY = height // 2


for seconds in range(1, 10001):
    field = [["."for j in range(width)]for i in range(height)]
    for index in range(0, len(robots), 2):
        x = (robots[index][0] + robots[index + 1][0]) % width
        y = (robots[index][1] + robots[index + 1][1]) % height
        robots[index][0] = x
        robots[index][1] = y
        field[y][x] = "o"

    for y in range(len(field) - 1):
        for x in range(len(field[0]) - 1):
            dx = 0
            while x+dx < len(field[0]) and field[y][x+dx] == "o":
                dx += 1
            if dx > 10:
                print(seconds)
                for line in field:
                    for char in line:
                        print(char, end=" ")
                    print()
                input("_"*width*2)