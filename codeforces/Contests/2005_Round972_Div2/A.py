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
  aval = "aeiou"

  rep = n // 5
  rem = n % 5

  res = []
  for let in aval:
    res += [let] * (rep + (1 if rem > 0 else 0))
    rem -= 1

  return "".join(res)

cases = int(input())
for _ in range(cases):
  print(solve())
