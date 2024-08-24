# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

n, k = [int(n) for n in input().split()]
cards = [int(n) for n in input().split()]

cards = cards[-k:] + cards[:-k]
for c in cards:
  print(c, end=' ')
