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

def possible(towel: str, visited=None) -> bool:
    if visited is None: visited = set()
    if not towel: return True
    if towel in visited: return False
    visited.add(towel)
    
    first_char = towel[0]
    if first_char in sorted_patterns:
        for pattern in sorted_patterns[first_char]:
            if towel.startswith(pattern):
                if possible(towel[len(pattern):], visited):
                    return True
    return False

result = 0
for index, towel in enumerate(towels):
    print(f"Processing towel {index + 1}/{len(towels)}: {towel}")
    if possible(towel):
        result += 1

print(result)