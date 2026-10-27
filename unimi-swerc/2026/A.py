*biglie, x = list(map(int, input().split()))

res = min(biglie[0], x)

if x > biglie[0] + biglie[1]:
    res -= x - (biglie[0] + biglie[1])

print(res)
