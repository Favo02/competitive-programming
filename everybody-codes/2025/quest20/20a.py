import sys

lines = list(map(lambda l: l.strip().replace(".", ""), sys.stdin.readlines()))

res = 0
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell != "T":
            continue
        if x != len(line)-1 and line[x+1] == "T":
            res += 1
        if y != len(lines)-1 and x % 2 == 1 and lines[y+1][x-1] == "T":
            res += 1

print(res)
