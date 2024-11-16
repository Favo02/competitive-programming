import sys

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

res = 0

for line in sys.stdin:
  n = int(line.strip())

  reached = {(n, 0)}

  while True:

    new_reached = set()
    found = float("inf")

    for r, steps in reached:
      for s in stamps:
        if r-s == 0:
          found = min(found, steps+1)
        if r-s >= 0:
          new_reached.add((r-s, steps+1))

    reached = new_reached

    if found != float("inf"):
      res += found
      break

print(res)

