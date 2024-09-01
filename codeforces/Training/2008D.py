# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  # lenght + list of numbers
  LEN = int(input())
  nums = [int(n) for n in input().split()]
  color = input()
  # print(LEN, nums, color)

  results = {}
  visited = set()

  for n in nums:
    if n in visited:
      continue

    cur = n
    black = 0
    while not cur in visited:
      # print(n, cur)
      if cur != n:
        results[cur] = (False, n)

      if color[cur-1] == "0":
        black += 1

      visited.add(cur)
      cur = nums[cur-1]

    # print("BL", n, black)
    results[n] = (True, black)

#
  # print(results)

  ress = []
  for i in range(1, LEN+1):
    valid, res = results[i]
    if valid:
      ress.append(res)
    else:
      valid, res = results[res]
      if valid:
        ress.append(res)

  return " ".join(map(str, ress))

cases = int(input())
for _ in range(cases):
  print(solve())
