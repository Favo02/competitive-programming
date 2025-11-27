from functools import reduce

nums = list(map(int, input().split(",")))

applied = []
for i, n in enumerate(nums):
    cur = 0
    for a in applied:
        if (i+1) % a == 0:
            cur += 1
    assert n-1 <= cur <= n
    if cur == n-1:
        applied.append(i+1)

print(reduce(lambda a, b: a*b, applied, 1))
