import sys
import heapq

def dijkstra(start, end):
  x, y = start
  queue = [(grid[y][x], x, y)]
  seen = set()
  while queue:
    dist, x, y = heapq.heappop(queue)
    if (x, y) in seen:
      continue
    seen.add((x, y))
    if (x, y) == end:
      return dist
    for dx, dy in [(+1, 0), (0, +1)]:
      nx, ny = x+dx, y+dy
      if not (0 <= nx < len(grid[0])): continue
      if not (0 <= ny < len(grid)): continue
      heapq.heappush(queue, (dist + grid[ny][nx], nx, ny))

grid = sys.stdin.read().strip().splitlines()
grid = [list(map(int, line.split())) for line in grid]

print(dijkstra((0,0), (14,14)))
