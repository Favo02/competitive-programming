cases = int(input())

for _ in range(cases):
    N = int(input())
    nums = list(map(int, input().split()))
    assert N == len(nums)
    nums = list(set(nums))
    nums.sort()
    # print(nums)

    res = [float('inf')] * N
    for n in nums:
        if n > N: continue
        res[n-1] = 1

    # print(res)

    limit = N
    bring = set(nums)
    for n in range(N):
        if res[n] == float('inf'): continue
        n += 1
        neww = set()
        # print("fix ", n)
        for b in bring:
            if n*b > N:
                limit = min(limit, b)
                continue
            # print("now", b, "=", n*b)
            res[n*b-1] = min(res[n*b-1], res[n-1] + res[b-1])
            neww.add(n*b)

        # bring.update(neww)
        bring = {b for b in bring | neww if b < limit}

    print(" ".join("-1" if n == float("inf") else str(n) for n in res))
