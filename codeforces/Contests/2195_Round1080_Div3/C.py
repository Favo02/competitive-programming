AD = {
    1: {2, 3, 4, 5},
    2: {1, 6, 3, 4},
    3: {1, 2, 5, 6},
    4: {1, 6, 2, 5},
    5: {1, 6, 3, 4},
    6: {2, 3, 4, 5},
}


def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == N

    dp = [[N + 1] * N for _ in range(6)]

    dp[nums[0] - 1][0] = 0

    for i in range(N):
        for n in range(6):
            malus = n + 1 != nums[i]

            if i == 0:
                dp[n][i] = int(malus)
                continue

            for ad in AD[n + 1]:
                dp[n][i] = min(dp[n][i], dp[ad - 1][i - 1] + malus)

    # for dpp in dp:
    # print(dpp)
    return min(dp[i][-1] for i in range(6))


for _ in range(int(input())):
    print(solve())
