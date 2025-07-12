from itertools import product

results = []
numbers = []
with open("data.txt") as f:
    for line in f:
        temp = line.split(": ")
        results.append(int(temp[0])) 
        numbers.append(list(map(int ,temp[1].split(" "))))

result = 0
for res, nums in zip(results, numbers):
    for ops in product(['+', '*'], repeat=len(nums) - 1):
        expression = nums[0]
        for i in range(len(ops)):
            if ops[i] == "*": expression *= nums[i+1]
            else: expression += nums[i+1]
        if expression == res:
            result += res
            break

print(result)