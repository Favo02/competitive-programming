import sys

lines = sys.stdin.readlines()
start = tuple(map(int, lines[0].strip().split("=")[1][1:-1].split(",")))
moves = lines[-1].strip().split("=")[1]
beacons = {
    line.strip().split("=")[0]: tuple(
        map(int, line.strip().split("=")[1][1:-1].split(","))
    )
    for line in lines[1:-1]
}

x, y = start
seen = {start}
for m in moves:
    bx, by = beacons[m]
    nx, ny = (x + bx) // 2, (y + by) // 2
    x, y = nx, ny
    seen.add((nx, ny))

fs = set()
for sx, sy in seen:
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        fs.add((sx + dx, sy + dy))
print(len(fs - seen))
