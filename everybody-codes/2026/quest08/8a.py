import sys

lines = list(map(list, map(str.strip, sys.stdin.readlines())))
ROWS, COLS = len(lines), len(lines[0])
starts = set()

for y, line in enumerate(lines):
    first = True
    for x, cell in enumerate(line):
        if y == 0 and cell != ".":
            starts.add((x, y))
        if cell != "." and first:
            first = False
            if y <= ROWS // 2:
                starts.add((x, y))

# print(starts)

used = set()
for x, y in starts:
    used.add((x, y))
    shadow = int(lines[y][x]) - 1
    while True:
        x += 1
        y += 1
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
print(len(used))

# for y, line in enumerate(lines):
#     for x, cell in enumerate(line):
#         if (x, y) in used:
#             print(cell, end="")
#         else:
#             print(".", end="")
#     print()
