nums = list(map(int, input().split(",")))

nails = 256
res = 0
prev = []

for a, b in zip(nums, nums[1:]):
    a, b = min(a, b), max(a, b)
    for c, d in prev:
        c, d = min(c, d), max(c, d)
        if (a < c or a > d) and (b > c and b < d) \
        or (b < c or b > d) and (a > c and a < d):
            res += 1
    prev.append((a, b))

print(res)
