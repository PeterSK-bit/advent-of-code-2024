import re
from itertools import permutations

with open("data.txt", "r") as f:
    data = [line.strip() for line in f]

antennas = {}
for y, line in enumerate(data):
    for match in re.finditer(r'[a-zA-Z0-9]', line):
        char = match.group()
        x = match.start()
        if char not in antennas:
            antennas[char] = []
        antennas[char].append((y, x))

antinodes = set()

for positions in antennas.values():
    if len(positions) < 2:
        continue
    
    for (y1, x1), (y2, x2) in permutations(positions, 2):
        dy, dx = y2 - y1, x2 - x1
        
        antinode1 = (y1 - dy, x1 - dx)
        antinode2 = (y2 + dy, x2 + dx)

        if 0 <= antinode1[0] < len(data) and 0 <= antinode1[1] < len(data[0]):
            antinodes.add(antinode1)
        if 0 <= antinode2[0] < len(data) and 0 <= antinode2[1] < len(data[0]):
            antinodes.add(antinode2)

print(len(antinodes))