from functools import cmp_to_key
import sys

op = {
  "+": lambda x: x+1,
  "-": lambda x: x-1,
  "=": lambda x: x
}

res = []
for line in sys.stdin:
  player, instruc = line.strip().split(":")
  instruc = instruc.split(",")

  cur_points = 10
  tot_points = 0
  i = 0
  while i < 10:
    cur_points = op[instruc[i%len(instruc)]](cur_points)
    tot_points += cur_points
    i+=1

  res.append((tot_points, player))

res.sort(reverse=True, key=cmp_to_key(lambda a, b: a[0] - b[0]))
print("".join(r[1] for r in res))
