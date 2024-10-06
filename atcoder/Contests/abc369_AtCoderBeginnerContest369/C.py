# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

n = int(input())
nums = [int(n) for n in input().split()]
# print(n, nums)

diffs = [b-a for a,b in zip(nums, nums[1:])]
# print(diffs)

if n == 1:
  print(1)
  exit()


res = 0

chunks = []
last = diffs[0]
cur = 1
for d in diffs[1:]:

  if d == last:
    cur += 1

  else:
    chunks.append(cur)
    last = d
    cur = 1
if cur != 0:
    chunks.append(cur)

res = n

for c in chunks:
  # print("chunk", c, c*(c+1) // 2)
  res += c*(c+1) // 2



# print(chunks)

print(res)

