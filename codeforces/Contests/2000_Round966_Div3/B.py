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
  seats = [int(n) for n in input().split()]
  # print(LEN, seats)

  aval = set()

  for s in seats:
    if len(aval) == 0:
      aval.add(s)
    else:
      if (s-1 not in aval) and (s+1 not in aval):
        return False
      else:
        aval.add(s)

  return True


cases = int(input())
for _ in range(cases):
  print("YES" if solve() else "NO")
