nums = list(map(int, input().split(",")))

res = 0
for c in range(90):
    for n in nums:
        if (c+1) % n == 0:
            res += 1

print(res)
