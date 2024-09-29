# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  n, k = [int(n) for n in input().split()]

  if k == 1:
    return n

  powers = [1]
  i = 1
  while powers[-1] < n:
    powers.append(k**i)
    i += 1

  pi = len(powers)-1
  res = 0
  while n != 0:

    while powers[pi] > n:
      pi -= 1

    if pi == 0:
      return res + n

    n -= powers[pi]
    res += 1

  return res

cases = int(input())
for _ in range(cases):
  print(solve())
  # print()
