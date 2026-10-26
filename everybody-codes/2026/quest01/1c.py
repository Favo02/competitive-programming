nums = list(map(int, input().split(",")))

res = 0
for n in nums:
    for i in range(3, 100000000, 2):
        if i * i - 1 >= n:
            res += abs(i * i - 1 - n)
            break

print(res)
