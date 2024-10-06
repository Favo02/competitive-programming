# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

inn = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
perm = input()
cur = perm.index("A")

res = 0
for c in inn[1:]:
  res += abs(cur - perm.index(c))
  cur = perm.index(c)

print(res)
