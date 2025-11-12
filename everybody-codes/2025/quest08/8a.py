nums = list(map(int, input().split(",")))

nails = 32
res = 0

for a, b in zip(nums, nums[1:]):
    a, b = min(a, b), max(a, b)
    if (b - a) % nails == nails // 2:
        res += 1

print(res)
