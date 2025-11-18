import sys

nums = list(map(int, sys.stdin.readlines()))

round = 0
while True:
    valid = False
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i] -= 1
            nums[i+1] += 1
            valid = True
    if not valid:
        break
    round += 1

while round < 10:
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            nums[i] -= 1
            nums[i-1] += 1
            valid = True
    round += 1

print(sum((i+1) * n for i, n in enumerate(nums)))
