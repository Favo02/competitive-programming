def solve():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    assert len(nums) == N
    assert K == 1
    k = int(input())
    k-=1
    target = nums[k]

    l = 0
    r = N-1
    res = 0

    while True:
        while l < k and (nums[l]+res) % 2 == target:
            l += 1
        while r > k and (nums[r]+res) % 2 == target:
            r -= 1
        if l == r == k:
            if res % 2 == 0:
                break
        res += 1

    print(res)

T = int(input())
for _ in range(T):
    solve()
