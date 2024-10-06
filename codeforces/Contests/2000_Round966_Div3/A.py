# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  n = input()
  if n[:2] != "10":
    return "NO"

  if len(n) <= 2:
    return "NO"

  if n[2] == "0":
    return "NO"

  if int(n[2:]) < 2:
    return "NO"

  return "YES"

cases = int(input())
for _ in range(cases):
  print(solve())
