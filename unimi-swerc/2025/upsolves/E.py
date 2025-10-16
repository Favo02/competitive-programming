n, a = map(int, input().split())

# input on multiple lines
nums = []
while len(nums) < n:
    nums += list(map(int, input().split()))
assert len(nums) == n
assert len(nums) > a

nums.sort()

res = nums[a-1] - nums[0]
for l in range(n-a+1):
    assert l+a-1 < len(nums)
    res = min(res, nums[l+a-1] - nums[l])
print(res)
