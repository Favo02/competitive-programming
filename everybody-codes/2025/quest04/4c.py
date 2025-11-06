import sys
from functools import reduce
from math import floor

lines = sys.stdin.readlines()
nums = (
    [(0, int(lines[0]))]
    + [tuple(map(int, t.split("|"))) for t in lines[1:-1]]
    + [(int(lines[-1]), 0)]
)

turns = reduce(lambda a, el: a * (el[0][1] / el[1][0]), zip(nums, nums[1:]), 1)
print(floor(turns * 100))
