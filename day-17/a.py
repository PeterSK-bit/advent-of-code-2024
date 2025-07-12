result = []

with open("data.txt", "r") as f:
    registers = [int(f.readline().split(": ")[1]) for _ in range(3)]
    f.readline() #empty line
    program = list(map(int, f.readline().split(": ")[1].split(",")))



index = 0
while index + 1 < len(program):
    values = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: registers[0],
        5: registers[1],
        6: registers[2]
    }
    match program[index]:
        case 0:
            registers[0] //= pow(2, values[program[index + 1]])
        case 1:
            registers[1] ^= values[program[index + 1]]
        case 2:
            registers[1] =values[program[index + 1]] % 8
        case 3:
            if registers[0] != 0:
                index =values[program[index + 1]]
                continue
        case 4:
            registers[1] ^= registers[2]
        case 5:
            result.append(values[program[index + 1]] % 8)
        case 6:
            registers[1] = registers[0] // pow(2,values[program[index + 1]])
        case 7:
            registers[2] = registers[0] // pow(2,values[program[index + 1]])
        case _:
            print("Value out of range")
    index += 2
print(*result, sep=",")