# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)


LEN = int(input())
nums = [int(n) for n in input().split()]
# print(LEN, nums)

ops = 0
while len([n for n in nums if n > 0]) > 1:
  nums.sort(reverse=True)
  nums[0] -= 1
  nums[1] -= 1
  # print(nums)
  ops+=1

print(ops)
