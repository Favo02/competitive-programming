# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  LEN = int(input())
  n = [int(n) for n in input().split()]
  s = list(input())
  # print(n, s)

  start, end = 0, LEN - 1
  res = 0

  pairs = []

  while start < end:

    while s[start] != "L":
      start += 1
      if start >= end:
        break

    while s[end] != "R":
      end -= 1
      if end <= start:
        break

    if start < end:
      # res += sum(n[start:end+1])
      pairs.append((start, end))
      s[start] = "S"
      s[end] = "E"

  mult = 0
  for nn, ss in zip(n, s):
    if ss == "S":
      mult += 1

    res += nn * mult

    if ss == "E":
      mult -= 1
  return res


cases = int(input())
for _ in range(cases):
  print(solve())
