# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def printm(matrix):
  for row in matrix:
    print(row)


def solve():

  height, width, k = [int(n) for n in input().split()]

  LEN = int(input())
  gorillas = [int(n) for n in input().split()]

  base = [min(n, k, width-k + 1) for n in range(1, (width+1)//2 +1)]

  matrix = []
  for mult in range(1, (height+1)//2 +1):
    matrix.append([min(n * min(min(mult, k), height-k + 1), k*k) for n in base])

  AVAL = []

  def multapp(k, times):
    for _ in range(times):
      AVAL.append(k)

  for r, row in enumerate(matrix):
    for c, val in enumerate(row):

      if (r == len(matrix)-1) and (c == len(row)-1):
        if (width % 2 == 0) and (height % 2 == 0):
          multapp(val, 4)
        elif (width % 2 == 0) or (height % 2 == 0):
          multapp(val, 2)
        else:
          AVAL.append(val)

      elif (r == len(matrix)-1):
        if height % 2 == 0:
          multapp(val, 4)
        else:
          multapp(val, 2)

      elif (c == len(row)-1):
        if width % 2 == 0:
          multapp(val, 4)
        else:
          multapp(val, 2)

      else:
        multapp(val, 4)


  assert len(AVAL) == height * width
  AVAL.sort(reverse=True)
  gorillas.sort(reverse=True)

  # print(f"w {width} h {height} k {k}")
  # printm(matrix)
  # print("GORI", gorillas)
  # print("AVAL", AVAL)

  res = 0
  for g, a in zip(gorillas, AVAL):
    # print(g, a)
    res += g * a


  return res

cases = int(input())
for _ in range(cases):
  print(solve())
