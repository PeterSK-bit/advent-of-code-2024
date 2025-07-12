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
    
    for pos in positions:
        antinodes.add(pos)
    
    for (y1, x1), (y2, x2) in permutations(positions, 2):
        dy, dx = y2 - y1, x2 - x1
        
        antinode1 = (y1 - dy, x1 - dx)
        antinode2 = (y2 + dy, x2 + dx)

        while 0 <= antinode1[0] < len(data) and 0 <= antinode1[1] < len(data[0]):
            antinodes.add(antinode1)
            antinode1 = (antinode1[0] - dy, antinode1[1] - dx)

        while 0 <= antinode2[0] < len(data) and 0 <= antinode2[1] < len(data[0]):
            antinodes.add(antinode2)
            antinode2 = (antinode2[0] + dy, antinode2[1] + dx)

print(len(antinodes))
#print(sorted(antinodes, key=lambda x: x[0]))

#1. nula (0,11) (3,2) (5,6) (7,5) (9,4) (11,3) (7,0)
#2. nula (1,3) (0,1) (4,9) (5,11) (0,6) (6,3) (8,2) (10,1)
#3. nula (2,10) (5,1)

#1. Ačko (11,10) (2,4) (1,3)
#2. Ačko (0,0) (1,1) (2,2) (3,3) (4,4) (5,5) (6,6) (7,7) (10,10) (11,11)