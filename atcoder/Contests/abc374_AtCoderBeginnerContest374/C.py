# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

dep = int(input())
deps = [int(n) for n in input().split()]
deps.sort(reverse=True)

def solve(a, b, i):
  if i == dep:
    return max(a, b)
  return min(solve(a+deps[i], b, i+1), solve(a, b+deps[i], i+1))

print(solve(0,0,0))
