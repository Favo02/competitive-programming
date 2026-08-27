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
print(len(seen))
