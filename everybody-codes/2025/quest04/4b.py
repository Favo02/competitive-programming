import sys
from functools import reduce
from math import ceil

nums = list(map(int, sys.stdin.readlines()))
turns = reduce(lambda a, el: a * (el[0] / el[1]), zip(nums, nums[1:]), 1)
print(ceil(10000000000000 / turns))
