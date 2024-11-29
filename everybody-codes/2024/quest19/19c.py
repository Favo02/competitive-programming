import sys
from collections import defaultdict
from operator import itemgetter

def left(r, c):
  temp = field[r-1][c-1]
  field[r-1][c-1] = field[r-1][c]
  field[r-1][c] = field[r-1][c+1]
  field[r-1][c+1] = field[r][c+1]
  field[r][c+1] = field[r+1][c+1]
  field[r+1][c+1] = field[r+1][c]
  field[r+1][c] = field[r+1][c-1]
  field[r+1][c-1] = field[r][c-1]
  field[r][c-1] = temp

def right(r, c):
  temp = field[r-1][c-1]
  field[r-1][c-1] = field[r][c-1]
  field[r][c-1] = field[r+1][c-1]
  field[r+1][c-1] = field[r+1][c]
  field[r+1][c] = field[r+1][c+1]
  field[r+1][c+1] = field[r][c+1]
  field[r][c+1] = field[r-1][c+1]
  field[r-1][c+1] = field[r-1][c]
  field[r-1][c] = temp

cell_positions_found = defaultdict(dict)
cell_cycle = {}
found_cycle = 0

def apply(time, cycle_detection=True):
  k = 0
  for r, row in enumerate(field):
    for c, cell in enumerate(row):
      if r == 0 or r == len(field)-1: continue
      if c == 0 or c == len(field[0])-1: continue

      op[key[k % len(key)]](r, c)
      k += 1

  if not cycle_detection: return

  global found_cycle

  for r, row in enumerate(field):
    for c, cell in enumerate(row):
      if cell == ".": continue
      if cell in cell_cycle: continue

      if (r,c) in cell_positions_found[cell]:
        cell_cycle[cell] = time
        found_cycle += 1
        continue

      cell_positions_found[cell][(r, c)] = time

key = input()
input()

field = []

symbol_count = defaultdict(int)
original_positions = {}

for r, line in enumerate(sys.stdin):
  line = line.strip()
  field.append(list(line))
  for c, cell in enumerate(line):
    if cell != ".":
      newname = f"{cell}{symbol_count[cell]}"

      field[r][c] = newname
      original_positions[newname] = (r, c)

      symbol_count[cell] += 1

assert symbol_count[">"] == 1
assert symbol_count["<"] == 1

TIME = 100 # example
TIME = 1_048_576_000

op = {"L": left, "R": right}

time = 0
while time < TIME and found_cycle < len(original_positions):
  apply(time)
  time += 1

field = [['.'] * len(field[0]) for _ in range(len(field))]

time_add_symbol = defaultdict(list)
for what, time in cell_cycle.items():
  time_add_symbol[TIME - (TIME % time)].append((what))

times = time_add_symbol.keys()
for time in range(min(times)-1, max(times)+1):
  apply(time)

  if time in time_add_symbol:
    for who in time_add_symbol[time]:
      r, c = original_positions[who]
      field[r][c] = who

for f in field:
  if ">0" in f:
    print("".join(map(itemgetter(0), f[f.index(">0")+1 : f.index("<0")])))
