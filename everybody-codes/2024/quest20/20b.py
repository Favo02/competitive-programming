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

MOVE = {"-": -2, ".": -1, "S": -1, "A": -1, "B": -1, "C": -1, "+": +1}
TO_VISIT = "ABC"

HEIGHT = 10000

queue = deque()
queue.append((0, *start, -1, -1, 0))

heights = defaultdict(int)
heights[(0, *start, -1, -1, 0)] = HEIGHT

while queue:
  cur = queue.popleft()
  time, x, y, px, py, found = cur
  height = heights[cur]

  if (x, y) == start and found == 3 and height >= HEIGHT:
    print(time)
    break

  for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
    nx, ny = dx + x, dy + y
    if not (0 <= nx < COLS): continue
    if not (0 <= ny < ROWS): continue
    if field[ny][nx] == "#": continue
    if nx == px and ny == py: continue

    newf = found
    if found < 3 and field[ny][nx] == TO_VISIT[found]:
      newf += 1

    newc = (time+1, nx, ny, x, y, newf)
    newh = height + MOVE[field[ny][nx]]

    if newh > heights[newc]:
      heights[newc] = newh
      queue.append(newc)
