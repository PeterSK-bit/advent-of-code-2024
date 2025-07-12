import time
start = time.time()

rules = []
queue = []
with open("data.txt") as f:
    temp = f.readlines()
    for index, rule in enumerate(temp):
        if rule == "\n":
            break
        rules.append(list(map(int,(rule.strip().split("|")))))

    for i in  temp[index+1:]:
        queue.append(list(map(int, i.split(","))))

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
    error = False
    index = 0
    while index < len(q):
        after = getPagesAfterPage(q[index])
        for elem in after:
            if elem in q[:index]:
                error = True
                q.insert(index+1, elem)
                q.remove(elem)
                index -= 1
        index += 1
    if error:
        result += q[len(q)//2]

print(f"{result=}")
print("runtime:" ,time.time() - start)