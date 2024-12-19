# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  N, K = map(int, input().split())

  res = [-1] * N

  n = 1
  for i in range(K-1, N, K):
    res[i] = n
    n += 1

  for i in range(N):
    if res[i] == -1:
      res[i] = n
      n += 1

  return ' '.join(map(str, res))

cases = int(input())
for _ in range(cases):
  print(solve())
