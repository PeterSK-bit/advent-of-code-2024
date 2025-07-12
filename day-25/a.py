def scan_process(scan, keys, locks):
    temp = [-1,-1,-1,-1,-1]
    for row in scan:
        for index, char in enumerate(row):
            temp[index] += char == "#"

    if scan[0] == "#####":
        locks.append(temp)
    else:
        keys.append(temp)


scan = []
locks = []
keys = []

with open("data.txt", "r") as f:
    for line in  f:
        line = line.strip()
        if not line:
            scan_process(scan, keys, locks)
            scan = []
            continue
        scan.append(line)

scan_process(scan, keys, locks) #for last input

result = 0
for lock in locks:
    for key in keys:
        result += all(key[index] + lock [index] < 6 for index in range(5))

print(result)