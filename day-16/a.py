from heapq import heappush, heappop

with open("data.txt", "r") as f:
    data = [line.strip() for line in f]

#find start and end
start = None
end = None
for y, line in enumerate(data):
    if line.find("S") != -1:
        start = (line.find("S"), y)
        if end: break
    if line.find("E") != -1:
        end = (line.find("E"), y)
        if start: break

def h_distance(a:tuple, b:tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#A*
visited = set()
came_from = dict()
f = 0 + h_distance(start, end)
# Initial direction: East
pq = [(f, 0, start, (1, 0))]  # f, g, coordinates, direction
g_score = {start: 0}

while pq:
    _, current_g, current, current_direction = heappop(pq)

    if (current, current_direction) in visited:
        continue
    visited.add((current, current_direction))

    if current == end:
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        break

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = current[0] + dx, current[1] + dy
        new_direction = (dx, dy)

        if data[ny][nx] != "#" and (nx, ny, new_direction) not in visited:
            rotation_cost = 1000 if new_direction != current_direction else 0
            g = current_g + 1 + rotation_cost
            if (nx, ny) not in g_score or g < g_score[(nx, ny)]:
                g_score[(nx, ny)] = g
                f = g + h_distance((nx, ny), end)
                heappush(pq, (f, g, (nx, ny), new_direction))
                came_from[(nx, ny)] = current

result = len(path) - 1 # -start
direction = (1, 0)
i = 0
for i in range(len(path)-1):
    x,y = path[i]
    nx ,ny = path[i+1]
    dx,dy = direction
    if (x+dx, y+dy) != (nx, ny):
        result += 1000
        direction = (nx - x, ny - y)

print(result)