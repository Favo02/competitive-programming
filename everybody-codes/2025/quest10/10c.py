import sys
from collections import defaultdict

def bfs(dp):
    newdp = [[defaultdict(int) for _ in range(COLS)] for _ in range(ROWS)]
    keep = False
    for y in range(ROWS):
        for x in range(COLS):
            for sh, ways in dp[y][x].items():
                sh = list(sh)

                dead = 0
                escaped = 0
                canmove = 0
                for sx, sy in enumerate(sh):
                    if grid[y][x] != "#" and sx == x and sy == y:
                        sh[sx] = -1

                    if sh[sx] == -1:
                        dead += 1
                        continue
                    if sh[sx] >= ROWS:
                        escaped += 1
                        continue

                    if grid[y][x] == "#" or sx != x or sy != y-1:
                        canmove += 1


                if dead == COLS:
                    global res
                    res += ways
                    continue

                if escaped > 0:
                    continue

                keep = True

                # special case: no sheep can move
                if canmove == 0:
                    for dx, dy in [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]:
                        nx, ny = x + dx, y + dy
                        if not (0 <= nx < COLS): continue
                        if not (0 <= ny < ROWS): continue
                        newdp[ny][nx][tuple(sh)] += ways
                    continue

                for sx, sy in enumerate(sh):
                    # sheep escaped or eaten
                    if sy == -1 or sy >= ROWS:
                        continue
                    # sheep walking into dragon position
                    if sy == y-1 and sx == x and grid[y][x] != "#":
                        continue

                    sh[sx] += 1
                    if sh[sx] >= ROWS:
                        sh[sx] -= 1
                        continue

                    for dx, dy in [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]:
                        nx, ny = x + dx, y + dy
                        if not (0 <= nx < COLS): continue
                        if not (0 <= ny < ROWS): continue
                        newdp[ny][nx][tuple(sh)] += ways

                    sh[sx] -= 1
    return keep, newdp

grid = list(map(str.strip, sys.stdin.readlines()))
ROWS, COLS = len(grid), len(grid[0])

dp = [[{} for _ in range(COLS)] for _ in range(ROWS)]

sheeps = [-1]*COLS
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell == "S":
            sheeps[x] = y
        if cell == "D":
            dragon = x, y

dp[dragon[1]][dragon[0]][tuple(sheeps)] = 1

res = 0
while True:
    keep, dp = bfs(dp)
    if not keep:
        break
print(res)
