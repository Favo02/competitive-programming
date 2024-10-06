# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

res = 0
for i in range(12):
  s = input()
  if len(s) == i+1:
    res += 1

print(res)
