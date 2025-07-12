l1 = []
l2 = []

with open("data.txt") as f:
    for line in f:
        temp = line.strip().split("   ")
        l1.append(int(temp[0]))
        l2.append(int(temp[1]))


result = 0

left_sorted = sorted(l1)
right_sorted = sorted(l2)
    
for left, right in zip(left_sorted, right_sorted):
    result += abs(left - right)

print(result)