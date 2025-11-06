import sys
from functools import reduce
from math import floor

nums = list(map(int, sys.stdin.readlines()))
turns = reduce(lambda a, el: a * (el[0] / el[1]), zip(nums, nums[1:]), 1)
print(floor(turns * 2025))
