# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

LEN = int(input())
enemies = [int(n) for n in input().split()]
# print(LEN, enemies)


i = 0
t = 0
while i < LEN:

  oneonethree = enemies[i] // 5
  enemies[i] -= oneonethree * 5
  t += oneonethree * 3

  while enemies[i] > 0:
    t += 1
    if t % 3 == 0:
      enemies[i] -= 3
    else:
      enemies[i] -= 1

  i += 1
  # print(t)


print(t)
