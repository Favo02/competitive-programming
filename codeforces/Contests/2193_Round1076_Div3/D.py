cases = int(input())

for _ in range(cases):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert n == len(A) == len(B)

    def sim(x):
        monst = 0
        sword = 0
        hits = 0
        while sword < n and monst < n:
            if A[sword] < x:
                sword += 1
                continue
            hits += 1
            sword += 1
            if hits == B[monst]:
                monst += 1
                hits = 0
        return x * monst

    A.sort()
    # print(A)
    # print(B)

    damage = len(A)
    prefix = [0]
    for b in B:
        prefix.append(prefix[-1] + b)
    prefix = prefix[1:]

    i = 0
    while i < n and prefix[i] <= damage:
        i += 1

    # print(damage, A)
    # print(prefix, i)

    res = i
    for s in A:
        res = max(res, i * s)
        # print(res)

        damage -= 1
        while i >= 0 and prefix[i-1] > damage:
            i -= 1
        # print(damage, i)

    print(res)
    # print()

    # sims = [sim(x) for x in range(max(A)+10)]
    # print(max(sims))

