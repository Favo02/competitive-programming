def solve(even, odd):
    if odd == 0:
        return []

    if even == 0 and odd == 1:
        return ["AAA"]

    if even == odd == 1:
        return [(1, 2)]

    if even > odd:
        return []

    if even == 0:
        if odd % 2 == 0:
            return []
        else:
            res = []
            for i in range(2, odd+1):
                res.append((1, i))
            return res

    res = []
    diff = (odd - even)
    i = 1
    if diff % 2 == 0:
        for i in range(1, 2*even):
            res.append((i, i+1))
        for ii in range(i+2, i+2 + diff):
            res.append((1, ii))

    else:
        for i in range(1, 2*even + 1):
            res.append((i, i+1))
        for ii in range(i+2, i+2 + diff - 1):
            res.append((1, ii))


    return res


C = int(input())
for _ in range(C):
    x, y = map(int, input().split())
    r = solve(x, y)
    if r:
        print("YES")
        for rr in r:
            if rr == "AAA":
                continue
            print(*rr)
    else:
        print("NO")
