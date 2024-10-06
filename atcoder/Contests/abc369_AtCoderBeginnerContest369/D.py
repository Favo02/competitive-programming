# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

import sys
sys.setrecursionlimit(10**8)

n = int(input())
nums = [int(n) for n in input().split()]

odd = [0 for _ in range(n)]
even = [0 for _ in range(n)]

maxodd = 0
maxeven = 0

for i, monster in enumerate(nums):

  if i == 0:
    even[0] = 0
    odd[0] = monster

    maxodd = monster

  else:
    odd[i] = maxeven + monster
    even[i] = maxodd + (monster*2)

    maxodd = max(maxodd, odd[i])
    maxeven = max(maxeven, even[i])

print(max(max(odd), max(even)))
