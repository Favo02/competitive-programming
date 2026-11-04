import sys

lines = [
    [int(d) if d != "." else d for d in l]
    for l in map(str.strip, sys.stdin.readlines())
]

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

round = 1
energy = 0
warriors = 0
while True:
    st = starts[(round - 1) % 6]
    dx, dy = dirs[(round - 1) % 6]

    nenergy = nwarriors = 0
    for x, y in st:
        shadow = 0
        while True:
            if not (0 <= x < COLS):
                break
            if not (0 <= y < ROWS):
                break
            if lines[y][x] == ".":
                break
            if lines[y][x] <= 0:
                lines[y][x] += 1
            newshadow = max(shadow - 1, lines[y][x] - 1)
            if int(lines[y][x]) > shadow and lines[y][x] > 0:
                lines[y][x] += 1
                energy += 1
                nenergy += 1
                if lines[y][x] > 9:
                    lines[y][x] = -3
                    warriors += 1
                    nwarriors += 1
            x, y = x + dx, y + dy
            shadow = newshadow

    # print(round, nenergy, nwarriors)
    # print(round, energy, warriors, nenergy, nwarriors)
    if warriors >= 100000:
        break
    # if round > 10:
    #     break
    round += 1

    # for y, line in enumerate(lines):
    #     for x, cell in enumerate(line):
    #         if cell == ".":
    #             print("..", end="")
    #         else:
    #             print(f"{cell:2d}", end="")
    #     print()
print(energy)
