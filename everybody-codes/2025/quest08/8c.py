nums = list(map(int, input().split(",")))

nails = 256
res = 0
prev = list(zip(nums, nums[1:]))

for a in range(1, nails+1):
    for b in range(a+1, nails+1):
        cur = 0
        for c, d in prev:
            c, d = min(c, d), max(c, d)
            if (a == c and b == d) \
            or (a < c or a > d) and (b > c and b < d) \
            or (b < c or b > d) and (a > c and a < d):
                cur += 1
        res = max(res, cur)

print(res)
