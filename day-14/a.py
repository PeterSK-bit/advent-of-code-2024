from math import prod

with open("data.txt", "r") as f:
    robots = []
    for line in f:
        pairs = line.strip().replace("p=", "").replace("v=", "").split(" ")
        for pair in pairs:
            x, y = map(int, pair.split(","))
            robots.append([x, y])

seconds = 100
width = 101
height = 103
midX = width // 2
midY = height // 2

quadrants = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
}

for index in range(0, len(robots), 2):
    x = (robots[index][0] + robots[index + 1][0] * seconds) % width
    y = (robots[index][1] + robots[index + 1][1] * seconds) % height

    if x < midX and y < midY: quadrants[0] += 1
    elif x > midX and y < midY: quadrants[1] += 1
    elif x < midX and y > midY: quadrants[2] += 1
    elif x > midX and y > midY: quadrants[3] += 1 

print(prod(quadrants.values()))