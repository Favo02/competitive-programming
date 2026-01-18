def solve():
    n, m, h = map(int, input().split())
    nums = list(map(int, input().split()))
    assert len(nums) == n

    orig = nums.copy()
    changed = [m+1] * n
    reset = -1

    for time in range(m):
        b, c = map(int, input().split())
        b -= 1

        # print("op", b, c)
        # print(nums)
        # print(changed, reset)


        if changed[b] <= reset:
            nums[b] = orig[b]

        changed[b] = time
        nums[b] += c

        if nums[b] > h:
            reset = time

        # print(nums)

    for i in range(n):
        if changed[i] <= reset:
            nums[i] = orig[i]

    print(" ".join(map(str, nums)))


cases = int(input())

for _ in range(cases):
    solve()
