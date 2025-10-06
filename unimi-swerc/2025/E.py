n, a = map(int, input().split())

nums = []
while len(nums) < n:
    nums += list(map(int, input().split()))

assert len(nums) == n

nums.sort()

l = 0
r = a - 1

res = nums[r] - nums[l]

if n == a:
    print(res)
else:
    while r < len(nums):
        res = min(res, nums[r] - nums[l])
        r += 1
        l += 1

    print(res)
