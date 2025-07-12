lst = []
with open("data.txt") as f:
    for item in f:
        lst.append(list(map(int, item.split(" "))))

result = 0
for l in lst:
    incresing = True if l[0] - l[-1] < 0 else False
    for index in range(len(l)-1):
        if abs(l[index] - l[index+1]) > 3 or (l[index] - l[index+1] >= 0 and incresing) or (l[index] - l[index+1] <= 0 and not incresing):
                break
    else:
        result += 1

print(result)