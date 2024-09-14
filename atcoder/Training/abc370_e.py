# from collections import deque
# from collections import Counter
from collections import defaultdict
# import heapq
# import bisect
from functools import lru_cache
# import math

import sys
sys.setrecursionlimit(10**8)

n, k = [int(n) for n in input().split()]
nums = [int(n) for n in input().split()]

places = defaultdict(list)
prefix = []
# places[0].append(0)

cur = 0
for i, n in enumerate(nums):
  places[cur].append(i)
  cur += n
  prefix.append(cur)
places[cur].append(i)

invalids = []
for i, p in enumerate(prefix):
  for s in places[p-k]:
    if s <= i:
      invalids.append((s, i))
    else:
      break

# print(invalids)

res = 0
mem = {}

def solve(start):

  if start in mem:
    return mem[start]

  if start == len(nums):
    return 1

  cur = 0
  for size in range(1, len(nums)-start+1):
    if (start, start+size-1) in invalids:
      continue
    cur += solve(start+size)

  mem[start] = cur
  return cur

res = solve(0)
print(res % 998244353)

# idea giusta, ma andava fatto con la programmazione dinamica
