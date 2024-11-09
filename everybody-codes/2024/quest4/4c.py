import sys

def dist(med):
  res = 0
  for n in nums:
    res += abs(n - med)
  return res

nums = []
for line in sys.stdin:
  nums.append(int(line.strip()))
nums.sort()

res = min(
  dist(nums[len(nums)//2 - 1]),
  dist(nums[len(nums)//2])
)

print(res)
