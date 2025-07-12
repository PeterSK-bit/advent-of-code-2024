from heapq import heappush, heappop

with open("data.txt", "r") as f:
    cords = [list(map(int, line.split(","))) for line in f]

start = (0,0)
end = (70,70)
width = 71
height = 71
nanoseconds = 1024

field = [["." for _ in range(width)] for __ in range(height)]

for x, y in cords[:nanoseconds]:
    field[y][x] = "#"

# --------------------------------------------------------------- #

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* alogrithm with weight 1 WRITTEN BY AI
def find_path(start, end, field, width, height):
    pq = []
    heappush(pq, (0, 0, start))  # (f(n), g(n), (x, y))
    visited = set()
    came_from = {}
    g_score = {start: 0}

    while pq:
        _, __, current = heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            if 0 <= nx < width and 0 <= ny < height and field[ny][nx] == "." and neighbor not in visited:
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + distance(neighbor, end)
                    heappush(pq, (f_score, tentative_g, neighbor))
                    came_from[neighbor] = current

    return None

path = find_path(start, end, field, width, height)
if path:
    #print(f"{path=}")
    print(f"result = {len(path) - 1}") # -1 because of (0, 0)
else:
    print("no path found")