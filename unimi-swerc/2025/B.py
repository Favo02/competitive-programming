n = int(input())
nums = list(map(int, input().split()))

res = 1
minn = nums[0]
for i in range(1, len(nums)):
    if nums[i] <= minn:
        res += 1
    minn = min(minn, nums[i])

print(res)
