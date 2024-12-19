# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  n = int(input())
  return n % 33 == 0

cases = int(input())
for _ in range(cases):
  print("Yes" if solve() else "No")
