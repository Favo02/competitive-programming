# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  ones, twos = [int(n) for n in input().split()]

  if twos % 2 == 0:

    if ones % 2 == 0:
      return True
    else:
      return False

  else:

    if ones % 2 == 0 and ones >= 2:
      return True
    else:
      return False



cases = int(input())
for _ in range(cases):
  print("YES" if solve() else "NO")
