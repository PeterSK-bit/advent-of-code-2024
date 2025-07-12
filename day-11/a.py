with open("data.txt", "r") as f:
    stones = list(map(int, f.readline().strip().split(" ")))
del f

for repeation in range(25):
    n = len(stones)
    index = 0
    while index < n:
        if stones[index] == 0:
            stones[index] = 1
        elif not len(str(stones[index])) % 2 :
            stoneString = str(stones[index])
            stones[index] = int(stoneString[:len(stoneString)//2])
            stones.insert(index+1, int(stoneString[len(stoneString)//2:]))
            index += 1
            n += 1
        else:
            stones[index] = stones[index] * 2024
        index += 1
    #print(repeation + 1, stones)
print(f"result = {len(stones)}")