import sys
from collections import deque, defaultdict

field = []
start = None
for line in sys.stdin:
  line = line.strip()
  field.append(line)
  if "S" in line:
    start = (line.index("S"), 0)

ROWS = len(field)
COLS = len(field[0])

MOVE = {"-": -2, ".": -1, "S": -1, "+": +1}
HEIGHT = 1000

res = 0

queue = deque()
queue.append((0, *start, -1, -1))

heights = defaultdict(int)
heights[(0, *start, -1, -1)] = HEIGHT

while queue:
  cur = queue.popleft()
  time, x, y, px, py = cur
  height = heights[cur]

  if time == 100:
    res = max(res, height)
    continue

  for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
    nx, ny = dx + x, dy + y
    if not (0 <= nx < COLS): continue
    if not (0 <= ny < ROWS): continue
    if field[ny][nx] == "#": continue
    if nx == px and ny == py: continue

    newc = (time+1, nx, ny, x, y)
    newh = height + MOVE[field[ny][nx]]

    if newh > heights[newc]:
      heights[newc] = newh
      queue.append(newc)

print(res)
