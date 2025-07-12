l1 = []
l2 = []

with open("data.txt") as f:
    for line in f:
        temp = line.strip().split("   ")
        l1.append(int(temp[0]))
        l2.append(int(temp[1]))

result = 0
for i in l1: result += i*l2.count(i)
print(result)