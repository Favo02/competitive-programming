from math import gcd, lcm

def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    input()
    assert N == len(nums)

    res = 0

    gcds = [gcd(a, b) for a, b in zip(nums, nums[1:])]

    # print(nums)
    # print(" ", gcds)

    for i in range(N):
        if i == 0:
            neww = gcds[0]
        elif i == N-1:
            neww = gcds[-1]
        else:
            neww = lcm(gcds[i-1], gcds[i])
        if neww < nums[i]:
            res += 1

    print(res)


t = int(input())
for _ in range(t):
    solve()
