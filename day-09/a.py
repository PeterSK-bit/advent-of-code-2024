with open("data.txt", "r") as f:
    data = f.readline()

memory = []
for index, num in enumerate(data):
    if index % 2 == 0:
        memory.extend([str(index // 2)] * int(num))
    else:
        memory.extend(["."] * int(num))

lIndex, rIndex = 0, len(memory) - 1
while lIndex < rIndex:
    if memory[lIndex] != ".":
        lIndex += 1
    elif memory[rIndex]  == ".":
        rIndex -= 1
    else:
        memory[lIndex], memory[rIndex] = memory[rIndex], memory[lIndex]
        lIndex += 1
        rIndex -= 1


result = 0
for index, num in enumerate(memory):
    if num == ".":
        break
    result += index*int(num)


print(result)
print(memory[:11])