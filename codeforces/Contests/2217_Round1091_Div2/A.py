def solve():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    assert len(nums) == N
    n = sum(nums)
    k = N*K

    if n % 2 == 1 or k % 2 == 0:
        print("YES")
    else:
        print("NO")


T = int(input())
for _ in range(T):
    solve()
