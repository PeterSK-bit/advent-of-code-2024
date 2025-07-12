with open("data.txt", "r") as f:
    patterns = []
    for line in f:
        if line == "\n":
            break
        patterns += line.strip().split(", ")
    towels = [line.strip() for line in f]

sorted_patterns = {}
for pattern in patterns:
    first_char = pattern[0]
    if first_char not in sorted_patterns:
        sorted_patterns[first_char] = [pattern]
    else:
        sorted_patterns[first_char].append(pattern)

def count_combinations(towel: str, memo = {}) -> int:
    if towel in memo:
        return memo[towel]
    
    if not towel:
        return 1
    
    total_combinations = 0
    first_char = towel[0]
    
    if first_char in sorted_patterns:
        for pattern in sorted_patterns[first_char]:
            if towel.startswith(pattern):
                total_combinations += count_combinations(towel[len(pattern):], memo)
    
    memo[towel] = total_combinations
    return total_combinations

total_result = 0
for index, towel in enumerate(towels):
    print(f"Processing towel {index + 1}/{len(towels)}: {towel}")
    total_result += count_combinations(towel)

print(f"{total_result=}")