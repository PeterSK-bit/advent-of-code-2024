import re

enabled = True

def validSubstring(string:str) -> str:
    global enabled # in case that line ends with don't()
    substring = ""

    while string:
        if enabled:
            index = string.find("don't()")
            if index == -1:
                substring += string
                break
            enabled = False
            substring += string[:index]
            string = string[index+7:]
        else:
            index = string.find("do()")
            if index == -1: break
            string = string[index+4:]
            enabled = True

    return substring

with open("data.txt") as f:
    data = f.readlines()
del f

result = 0
enabled = True

for string in data:
    string = validSubstring(string)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, string)

    for x, y in matches:
        result += int(x) * int(y)
    
print(result)