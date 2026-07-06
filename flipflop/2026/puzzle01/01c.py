import sys

nums = list(map(int, sys.stdin.readlines()))
L = len(nums)
res = 0

for t, pt in zip(nums[:L//2], nums[L//2:]):
    res += max(0, pt - int(t))
    res += max(0, int(t) - pt) * 5

print(res)
