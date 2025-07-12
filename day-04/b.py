with open("data.txt") as f:
    data = list(map(lambda x: x.strip(), f.readlines()))
del f

result = 0
for y in range(len(data)-2):
    for x in range(len(data[0])-2):
        string1 = data[y][x] + data[y+1][x+1] + data[y+2][x+2]
        string2 = data[y][x+2] + data[y+1][x+1] + data[y+2][x]
        if (string1 == "MAS" or string1 == "SAM") and (string2 == "MAS" or string2 == "SAM"):
            result += 1

print(result)