pairs = {}
with open("data.txt", "r") as f:
    for line in f:
        left, right = line.strip().split("-")
        pairs.setdefault(left, set()).add(right)
        pairs.setdefault(right, set()).add(left)

triangles = set()

for a in pairs:
    for b in pairs[a]:
        if b > a:
            common = pairs[a] & pairs[b]
            for c in common:
                if c > b:
                    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                        triangles.add((a, b, c))

print(f"result = {len(triangles)}")