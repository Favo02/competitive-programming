m, h = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

dists = [abs(m-h) for m in nums]
# print(dists)
# print(nums)
# print(h)
from math import gcd
print(gcd(*dists))
