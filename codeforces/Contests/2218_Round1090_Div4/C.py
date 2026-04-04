C = int(input())
for _ in range(C):
    n = int(input())
    res = []
    small = 1
    big = 3*n

    while len(res) < 3*n:
        res.append(big)
        res.append(big-1)
        big -= 2
        res.append(small)
        small += 1

    print(*res)
