def nexts(r, c):
  # hor
  if c <= 3:
    yield {(r,c+i) for i in range(4)}
  # ver
  if r <= 2:
    yield {(r+i,c) for i in range(4)}
  # diag1
  if c <= 3 and r <= 2:
    yield {(r+i,c+i) for i in range(4)}
  # diag2
  if c >= 3 and r <= 2:
    yield {(r+i,c-i) for i in range(4)}

def won(cells, target):
  return all(field[r][c] == target for r, c in cells)

def solve():
  wins = []
  allwins = set()

  for r in range(6):
    for c in range(7):
      for cells in nexts(r, c):
        if won(cells, "F"):
          wins.append(("F", cells))
          allwins.update(cells)
        if won(cells, "C"):
          wins.append(("C", cells))
          allwins.update(cells)

  valid_wins = []

  for winner, cells in wins:
    valid = True
    for r, c in cells:
      for rrr in range(r+1, 6):
        if (rrr, c) in cells: continue
        if (rrr, c) in allwins:
          valid = False
    if valid:
      valid_wins.append(winner)

  if "F" in valid_wins and "C" in valid_wins:
    return "?"
  if "F" in valid_wins:
    return "F"
  if "C" in valid_wins:
    return "C"
  if len(wins) > 0:
    return "?"
  return "0"

cases = int(input())
for i in range(cases):
  assert input() == ""
  field = [input() for _ in range(6)]

  # for f in field:
    # print(list(f))
  print(f"Case #{i+1}: {solve()}")
  # print()
