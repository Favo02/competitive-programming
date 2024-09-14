# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

s = list(input())
t = list(input())

res = []

for i in range(len(s)):
  if s[i] > t[i]:
    s[i] = t[i]
    # print("".join(s))
    res.append("".join(s))

# print(res)

# print("--")
# print(s)
# print(t)

for i in range(len(s)-1, -1, -1):
  # print(i, s[i], t[i])
  if s[i] != t[i]:
    s[i] = t[i]
    # print("".join(s))
    res.append("".join(s))

print(len(res))
for r in res:
  print(r)
