import sys
from collections import deque, defaultdict

def power(string):
  res = 0
  for i, r in enumerate(string):
    assert r != "."
    res += (ord(r) - ord("A") + 1) * (i+1)
  return res

def get_dir(r, c, dr, dc):
  found = set()
  placed = set()

  cr = r+dr
  cc = c+dc

  while len(found) < 2:

    if field[cr][cc] == "?" or field[cr][cc].isupper():
      found.add((field[cr][cc], cr, cc))

    if field[cr][cc].islower():
      placed.add(field[cr][cc].upper())

    cr+=dr
    cc+=dc

  return found, placed

field = []
queue = deque()

for r, line in enumerate(sys.stdin):
  field.append(list(line.strip()))
  for c, cell in enumerate(line.strip()):
    if cell == ".":
      queue.append((r, c))

seen = set()
while queue:
  r, c = queue.popleft()
  if (len(queue), r, c) in seen:
    break
  seen.add((len(queue), r, c))

  if field[r][c] != ".": continue

  valid = []

  (right, rplaced), (left, lplaced) = get_dir(r, c, 0, -1), get_dir(r, c, 0, +1)
  hor = {h for h in (right | left) if h[0] not in (rplaced | lplaced)}

  (up, uplaced), (down, dplaced) = get_dir(r, c, -1, 0), get_dir(r, c, +1, 0)
  vert = {v for v in (up | down) if v[0] not in (uplaced | dplaced)}

  if len(vert) == len(hor) == 1:
    v, rv, cv = vert.pop()
    h, rh, ch = hor.pop()

    if v == h != "?":
      field[r][c] = v.lower()
    elif v == "?" and h.isupper():
      field[r][c] = h.lower()
      field[rv][cv] = h
    elif v.isupper() and h == "?":
      field[r][c] = v.lower()
      field[rh][ch] = v
    else:
      queue.append((r, c))

    continue

  for (v, rv, cv) in vert:
    for (h, rh, ch) in hor:
      if v == h:
        valid.append((v, (rv, cv), (rh, ch)))

  if len(valid) == 1:
    v, (rv, cv), (rh, ch) = valid[0]
    field[r][c] = v.lower()

  else:
    queue.append((r, c))

fields = defaultdict(list)

for r, row in enumerate(field):
  for c, cell in enumerate(row):
    if cell.islower():
      fields[(r // 6, c // 6)].append(cell)

res = 0
for (r, c), word in fields.items():
  if len(word) == 4*4:
    res += power(map(str.upper, word))

