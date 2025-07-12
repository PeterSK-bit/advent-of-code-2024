import re

with open("data.txt") as f:
    data = f.readlines()
del f

result = 0

for string in data:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, string)
    
    for x, y in matches:
        result += int(x) * int(y)
    
print(result)