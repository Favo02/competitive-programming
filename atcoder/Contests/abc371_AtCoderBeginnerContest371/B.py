# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)


fam, bab = [int(n) for n in input().split()]

res = [False] * fam

for _ in range(bab):
  family, gender = input().split()
  family = int(family)
  if gender == "M" and not res[family-1]:
    print("Yes")
    res[family-1] = True
  else:
    print("No")
