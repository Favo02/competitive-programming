import sys
from collections import deque

OPS = {
  "ADD": lambda x, y: (x + y) % 1073741824,
  "SUB": lambda x, y: (x - y) % 1073741824,
  "MULTIPLY": lambda x, y: (x * y) % 1073741824,
}

def pprint():
  for l in grid:
    print(l)
  print()

def transpose(grid):
  return [[row[i] for row in grid] for i in range(len(grid[0]))]

def shift(who, num, amt):
  global grid
  assert who in ["ROW", "COL"]

  if who == "ROW":
    grid[num] = grid[num][-amt:] + grid[num][:-amt]
  else:
    grid = transpose(grid)
    shift("ROW", num, amt)
    grid = transpose(grid)

def op(opp, amt, who, num):
  global grid
  assert opp in ["ADD", "SUB", "MULTIPLY"]
  assert who in ["ROW", "COL", "ALL"]

  apply = OPS[opp]

  if who == "ALL":
    for y, row in enumerate(grid):
      for x, val in enumerate(row):
        grid[y][x] = apply(val, amt)
  elif who == "ROW":
    for x, val in enumerate(grid[num]):
      grid[num][x] = apply(val, amt)

  else:
    grid = transpose(grid)
    op(opp, amt, "ROW", num)
    grid = transpose(grid)

def act(inst):
  tokens = inst.split()
  assert tokens[0] in ["SHIFT", "ADD", "SUB", "MULTIPLY"]
  if tokens[0] == "SHIFT":
    shift(tokens[1], int(tokens[2])-1, int(tokens[4]))
  elif tokens[2] == "ALL":
    op(tokens[0], int(tokens[1]), tokens[2], 0)
  else:
    op(tokens[0], int(tokens[1]), tokens[2], int(tokens[3])-1)

grid, instructions, flow = sys.stdin.read().strip().split("\n\n")
grid = [[int(n) for n in line.split()] for line in grid.splitlines()]
instructions = deque(instructions.splitlines())

for fl in flow.splitlines():
  assert fl in ["TAKE", "CYCLE", "ACT"]
  if fl == "CYCLE":
    instructions.append(instructions.popleft())
  if fl == "ACT":
    act(instructions.popleft())

assert grid == transpose(transpose(grid))

print(max(max(sum(row) for row in grid), max(sum(row) for row in transpose(grid))))
