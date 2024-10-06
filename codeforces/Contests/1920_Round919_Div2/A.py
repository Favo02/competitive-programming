cases = int(input())

for _ in range(cases):

  CONSTRAINTS = int(input())

  GE = 1 # greather or equal
  LE = 2 # smaller or equal
  NE = 3 # not equal

  ge = -1
  le = float("inf")
  different = set()

  for _ in range(CONSTRAINTS):
    c, x = [int(n) for n in input().split()]
    if c == GE:
      ge = max(x, ge)
    elif c == LE:
      le = min(x, le)
    elif c == NE:
      different.add(x)
    else:
      assert False


  res = le-ge + 1

  if res > 0:
    for d in different:
      if d >= ge and d <= le:
        res -= 1

  print(max(0, res))
