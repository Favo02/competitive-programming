import sys

nums = []
for line in sys.stdin:
  nums.append(int(line.strip()))

MIN = min(nums)

res = 0
for n in nums:
  res += n - MIN

print(res)
