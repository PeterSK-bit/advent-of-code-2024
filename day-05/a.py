rules = []
queue = []
with open("data.txt") as f:
    temp = f.readlines()
    for index, rule in enumerate(temp):
        if rule == "\n":
            break
        rules.append(tuple(map(int,(rule.strip().split("|")))))

    for i in  temp[index+1:]:
        queue.append(tuple(map(int, i.split(","))))

del f, temp

def getPagesAfterPage(page) -> list:
    global rules
    result = []
    for rule in rules:
        if rule[0] == page:
            result.append(rule[1])
    return result

result = 0
for i, q in enumerate(queue):
    for index, page in enumerate(q):
        after = getPagesAfterPage(page)
        if any(elem in q[:index] for elem in after):
            print(i, "incorrect")
            break
    else:
        result += q[len(q)//2]

print(result)