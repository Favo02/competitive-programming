import sys

lines = list(map(list, map(str.strip, sys.stdin.readlines())))
ROWS, COLS = len(lines), len(lines[0])
starts = [set() for _ in range(6)]
dirs = [
    (+1, +1),
    (-1, +1),
    (-2, 0),
    (-1, -1),
    (+1, -1),
    (+2, 0),
]

for y, line in enumerate(lines):
    first = True
    for x, cell in enumerate(line):
        if cell == ".":
            continue

        if y == 0:
            starts[0].add((x, y))
            starts[1].add((x, y))
        if y == ROWS - 1:
            starts[3].add((x, y))
            starts[4].add((x, y))

        if first:
            first = False
            starts[5].add((x, y))
            if y <= ROWS // 2:
                starts[0].add((x, y))
            if y >= ROWS // 2:
                starts[4].add((x, y))

        if not any(c != "." for c in line[x + 1 :]):
            starts[2].add((x, y))
            if y <= ROWS // 2:
                starts[1].add((x, y))
            if y >= ROWS // 2:
                starts[3].add((x, y))

# print(starts)

ans = 0
for st, (dx, dy) in zip(starts, dirs):
    used = set()
    for x, y in st:
        used.add((x, y))
        shadow = int(lines[y][x]) - 1
        while True:
            x, y = x + dx, y + dy
            if not (0 <= x < COLS):
                break
            if not (0 <= y < ROWS):
                break
            if lines[y][x] == ".":
                break
            if int(lines[y][x]) > shadow:
                used.add((x, y))
            shadow = max(shadow - 1, int(lines[y][x]) - 1)

    # print(used)
    # for y, line in enumerate(lines):
    #     for x, cell in enumerate(line):
    #         if (x, y) in used:
    #             print(cell, end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print(len(used))
    ans += len(used)

print(ans)
