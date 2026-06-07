def solve(N, nums):

    res = []

    for el in range(N):
        water = [float("inf")] * N
        water[el] = 0

        wall = 0
        for i in range(N-1):
            n = nums[(el + i) % N]
            water[(el + i + 1) % N] = max(wall, n)
            wall = max(wall, n)

        wall = 0
        for i in range(N-1):
            n = nums[(el - i - 1) % N]
            water[(el - i - 1) % N] = min(water[(el - i - 1) % N], max(wall, n))
            wall = max(wall, n)

        res.append(sum(water))
    return res


T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == N

    print(*solve(N, nums))
