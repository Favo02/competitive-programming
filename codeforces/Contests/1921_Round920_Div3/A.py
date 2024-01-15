cases = int(input())

for _ in range(cases):

  x1 = None
  x2 = None
  y1 = None
  y2 = None
  for _ in range(4):
    x, y = [int(n) for n in input().split()]
    x1 = min(x1, x) if x1 != None else x
    x2 = max(x2, x) if x2 != None else x

    y1 = min(y1, y) if y1 != None else y
    y2 = max(y2, y) if y2 != None else y


  print((x2-x1) * (y2-y1))
