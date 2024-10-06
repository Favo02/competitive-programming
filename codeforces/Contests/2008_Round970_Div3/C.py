# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  start, end = [int(n) for n in input().split()]

  gap = 1
  cur = start
  res = 0

  while cur <= end:
    res += 1

    cur += gap
    gap += 1
    # print(cur, end=" ")
  # print()
  return res

cases = int(input())
for _ in range(cases):
  print(solve())
