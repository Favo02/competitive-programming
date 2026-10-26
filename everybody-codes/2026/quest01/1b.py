nums = list(map(int, input().split(",")))

res = 0
for n in nums:
    for i in range(3, 100000):
        req = i * 2 + (i - 2) * 2
        if req >= n:
            res += abs((req) - n)
            break

print(res)
