with open("data.txt", "r") as f:
    initial_stones = list(map(int, f.readline().strip().split(" ")))

stone_count = {}
for stone in initial_stones:
    stone_count[stone] = stone_count.get(stone, 0) + 1

for repeation in range(75):
    new_stone_count = {}
    for stone, count in stone_count.items():
        if stone == 0:
            new_stone_count[1] = new_stone_count.get(1, 0) + count
        elif stone >= 10 and (len(str(stone)) % 2 == 0):
            half_len = len(str(stone)) // 2
            left_part = int(str(stone)[:half_len])
            right_part = int(str(stone)[half_len:])
            new_stone_count[left_part] = new_stone_count.get(left_part, 0) + count
            new_stone_count[right_part] = new_stone_count.get(right_part, 0) + count
        else:
            new_stone_count[stone * 2024] = new_stone_count.get(stone * 2024, 0) + count
    
    stone_count = new_stone_count
   # print(f"Iteration {repeation + 1}: {sum(stone_count.values())} stones")

print(f"Final result: {sum(stone_count.values())}")
# 236804088748754