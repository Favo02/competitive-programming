cases = int(input())

deb = print


for _ in range(cases):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert n == len(A) == len(B)

    res = [-1]
    for a, b in zip(reversed(A), reversed(B)):
        res.append(max(res[-1], a, b))
    res = list(reversed(res[1:]))

    prefix = [0]
    for n in res:
        prefix.append(prefix[-1] + n)
    # print(prefix)

    for _ in range(q):
        l, r = map(int, input().split())
        # deb("q", l, r)
        print(prefix[r] - prefix[l-1], end=" ")
    print()
