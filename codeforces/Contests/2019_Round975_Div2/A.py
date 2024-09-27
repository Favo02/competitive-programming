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

  if len(nums) == 1:
    return nums[0] + 1

  a = len(nums[::2]) + max(nums[::2])
  b = len(nums[1::2]) + max(nums[1::2])
  return max(a,b)

cases = int(input())
for _ in range(cases):
  print(solve())
