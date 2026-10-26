nums = list(map(int, input().split(",")))

res = 0
for n in nums:
    for i in range(1000):
        if i * i >= n:
            res += abs(i * i - n)
            break

print(res)
