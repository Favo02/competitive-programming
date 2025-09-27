from collections import deque

NEAR = ((0, 1), (1, 0), (-1, 0), (0, -1))

ROWS, COLS = map(int, input().split())

queue = deque()
seen = set()
black = set()

grid = []

for y in range(ROWS):
    line = input()
    grid.append([0 if c == "." else 1 for c in line])
    for x, c in enumerate(line):
        if c == "#":
            grid[y][x] = "#"
            black.add((x, y))
            queue.append((x, y))

def inc(x, y):
    for nx, ny in NEAR:
        if not (0 <= y + ny < ROWS): continue
        if not (0 <= x + nx < COLS): continue
        if (x + nx, y + ny) in black: continue
        grid[y + ny][x + nx] += 1

for x, y in black:
    inc(x, y)

# print(queue)

# for g in grid:
#     print("".join(map(str, g)))
# print()

toapply = []

while True:
    while queue:
        x, y = queue.popleft()
        # assert (x, y) not in black
        for nx, ny in NEAR:
            if not (0 <= y + ny < ROWS): continue
            if not (0 <= x + nx < COLS): continue
            if (x + nx, y + ny) in black: continue
            if grid[y + ny][x + nx] == 1:
                toapply.append((x + nx, y + ny))
    for x, y in toapply:
        black.add((x, y))
        grid[y][x] = "#"
        queue.append((x, y))
        inc(x, y)
    if not toapply: break
    toapply.clear()

# for g in grid:
#     print("".join(map(str, g)))

print(len(black))
