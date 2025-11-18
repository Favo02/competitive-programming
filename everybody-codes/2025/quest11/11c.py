import sys

nums = list(map(int, sys.stdin.readlines()))
assert nums == sorted(nums), "input for part 3 skips first phase exchanges"

avg = sum(nums) // len(nums)
round = 0

nums = [n for n in nums if n > avg]
nums = list(reversed(nums))

for i in range(len(nums)-1):
    round += (nums[i] - nums[i+1]) * (i+1)
round += (nums[-1] - avg) * len(nums)

print(round)
