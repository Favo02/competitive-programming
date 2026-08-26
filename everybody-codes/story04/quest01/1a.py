import sys

lines = sys.stdin.readlines()

res = 0
for line in lines:
    nums = [int(n) for n in line.strip().split(",")]
    seen = set()
    cur = 0
    for j in nums:
        if (cur - j) > 0 and (cur - j) not in seen:
            cur = cur - j
        else:
            cur = cur + j
        seen.add(cur)
    res += cur
print(res)
