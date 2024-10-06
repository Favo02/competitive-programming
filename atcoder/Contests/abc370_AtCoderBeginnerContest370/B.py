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
elems = []

for _ in range(n):
  elems.append([int(n) for n in input().split()])

i = 1
for j in range(1, n+1):

  # print("comb", i, j)

  if i >= j:
    i = elems[i-1][j-1]
  else:
    i = elems[j-1][i-1]

print(i)
