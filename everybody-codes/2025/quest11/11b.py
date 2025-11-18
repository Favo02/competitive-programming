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

while not all(a == b for a, b in zip(nums, nums[1:])):
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            nums[i] -= 1
            nums[i-1] += 1
            valid = True
    round += 1

print(round)
