# just wait for it

with open("data.txt", "r") as f:
    data = f.readline().strip()

memory = []
# Populate the memory
for index, num in enumerate(data):
    if index % 2 == 0:
        memory.extend([str(index // 2)] * int(num))
    else:
        memory.extend(["."] * int(num))

lIndex, rIndex = 0, len(memory) - 1
while rIndex > 0:
    while lIndex < rIndex and memory[lIndex] != ".":
        lIndex += 1

    while lIndex < rIndex and memory[rIndex] == ".":
        rIndex -= 1

    gapLength = 0
    while lIndex + gapLength < len(memory) and memory[lIndex + gapLength] == ".":
        gapLength += 1

    fileLength = 0
    while rIndex - fileLength >= 0 and memory[rIndex - fileLength] == memory[rIndex]:
        fileLength += 1

    if gapLength >= fileLength:
        for i in range(fileLength):
            memory[lIndex + i], memory[rIndex - fileLength + 1 + i] = memory[rIndex - fileLength + 1 + i], "."
        lIndex = 0
        rIndex -= fileLength
    else:
        lIndex += gapLength
        if lIndex >= rIndex:
            rIndex -= fileLength
            lIndex = 0


result = 0
for index, num in enumerate(memory):
    if num == ".": continue
    result += index * int(num)

print(result)