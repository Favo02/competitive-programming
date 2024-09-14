# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

h, w, q = [int(n) for n in input().split()]

field = []
for _ in range(h):
  field.append([True] * w)

def printf():
  for row in field:
    print("".join(map(lambda x: "1" if x else "0", row)))

walls = h * w

for _ in range(q):
  y, x = [int(n) for n in input().split()]
  y -= 1
  x -= 1

  if field[y][x]:
    field[y][x] = False
    walls -= 1

  else:

    # top
    yy = y-1
    while yy >= 0 and not field[yy][x]:
      yy -= 1
    if yy >= 0:
      field[yy][x] = False
      walls -= 1

    # down
    yy = y+1
    while yy < h and not field[yy][x]:
      yy += 1
    if yy < h:
      field[yy][x] = False
      walls -= 1

    # left
    xx = x-1
    while xx >= 0 and not field[y][xx]:
      xx -= 1
    if xx >= 0:
      field[y][xx] = False
      walls -= 1

    # right
    xx = x+1
    while xx < w and not field[y][xx]:
      xx += 1
    if xx < w:
      field[y][xx] = False
      walls -= 1

  # printf()

print(walls)

# andava fatto con le posizioni al posto che tutta la matrice.
# si cerca con una bisearch il primo elemento prima e dopo del punto colpito e viene tolto
