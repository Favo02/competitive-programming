# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)


# lenght + list of numbers
n = int(input())


res = 0
lastL = None
lastR = None

for _ in range(n):
  key, hand = input().split()
  key = int(key)
  # print(key, hand)

  if hand == 'L':
    if lastL is None:
      lastL = key
    else:
      res += abs(key - lastL)
      lastL = key

  if hand == 'R':
    if lastR is None:
      lastR = key
    else:
      res += abs(key - lastR)
      lastR = key

print(res)
