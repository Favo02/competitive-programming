# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys
from bisect import bisect_left, bisect_right

# sys.setrecursionlimit(10**5)

def solve():

  # lenght + list of numbers
  p, q = [int(n) for n in input().split()]
  points = [int(n) for n in input().split()]
  queries = [int(n) for n in input().split()]

  # print(p, q)
  # print(points)

  res = {}

  points_val = []
  cur = 0
  for i, p in enumerate(points):
    cur += len(points)-1 - i
    cur -= max(0, (i-1))
    points_val.append(cur)
    if cur in res:
      res[cur] += 1
    else:
      res[cur] = 1

  # print(points)
  # print(points_val)
  # print(res)

  for i in range(1, len(points)):
    a, b = (points[i-1], points[i])
    if a+1 == b:
      continue


    cur = points_val[i-1] - (i-1)

    # print(i, cur, b-a-1)

    if cur in res:
      res[cur] += b-a-1
    else:
      res[cur] = b-a-1

  for q in queries:
    if q in res:
      print(res[q], end=" ")
    else:
      print(0, end=" ")
  print()

cases = int(input())
for _ in range(cases):
  solve()
