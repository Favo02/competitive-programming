# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

cur = 0
lastt = 0

N = int(input())
for _ in range(N):
  t, qty = map(int, input().split())
  cur = max(0, cur - abs(t - lastt))
  # print(t, cur)
  cur += qty

  # print(t, cur)

  lastt = t

print(cur)
