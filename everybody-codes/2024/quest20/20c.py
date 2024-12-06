import sys

# WARNING! BIG ASSERTION ON INPUT FORMAT:
# there is a single column which is the best one, true in example and my input

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
HEIGHT = 384400

def best_col():

  best = (-float("inf"), -1)

  for x in range(COLS):
    h = 0
    for y in range(ROWS):
      if field[y][x] == "#":
        h = -float("inf")
        break
      h += MOVE[field[y][x]]

    if h > best[0] or\
       h == best[0] and abs(start[0]-x) < abs(start[0]-best[1]):
      best = (h, x)

  return best

diff, x, y = *best_col(), 0
h = HEIGHT - abs(x - start[0])

# skip entire fields
while h+diff > 0:
  y += ROWS
  h += diff

# walk single cell
while h > 0:
  y += 1
  h += MOVE[field[y % ROWS][x]]

print(y)
