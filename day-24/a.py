wires = {}

with open("data.txt", "r") as f:
    for line in f:
        if line == "\n": break
        left, right = line.strip().split(": ")
        wires[left] = int(right)
    
    operations = [line.strip().split(" ")[:3] + line.strip().split(" ")[4:] for line in f]

def bit_calculate(left:int, right:int, operation:str) -> int:
    match operation:
        case "OR": #|
            return left | right
        case "AND": #&
            return left & right
        case "XOR": #^
            return left ^ right

def recursion(popIndex = 0):
    left, operation, right, result = operations.pop(popIndex)

    if left not in wires:
        lindex = next((i for i in range(len(operations)) if operations[i][-1] == left), None)
        recursion(lindex)
    if right not in wires:
        rindex = next((i for i in range(len(operations)) if operations[i][-1] == right), None)
        recursion(rindex)

    wires[result] = bit_calculate(wires[left], wires[right], operation)

while operations:
    recursion()

filtered_sorted_dict = {
    key: wires[key]
    for key in sorted(wires.keys(), reverse=True)
    if key.startswith("z")
}

result = "".join(map(str, filtered_sorted_dict.values()))

print(int(result, 2))