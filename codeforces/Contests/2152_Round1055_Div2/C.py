from bisect import bisect_left

cases = int(input())

def solve():
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    assert len(nums) == n

    # print(nums)

    zeros = [0]
    ones = [0]
    for n in nums:
        if n == 0:
            zeros.append(zeros[-1] + 1)
            ones.append(ones[-1])
        else:
            zeros.append(zeros[-1])
            ones.append(ones[-1] + 1)

    consecutive = []
    for i, (a, b) in enumerate(zip(nums, nums[1:])):
        if a == b:
            consecutive.append(i)
    # print(consecutive)

    def query():
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        # print("--")
        # print(l, r, nums[l:r+1])

        assert r >= l
        if r - l < 2:
            return -1

        ze, on = zeros[r+1] - zeros[l], ones[r+1] - ones[l]
        if ze % 3 != 0: return -1
        if on % 3 != 0: return -1

        if not consecutive:
            return 1 + (ze // 3) + (on // 3)

        bis = bisect_left(consecutive, l)
        if (bis < len(consecutive)) and (consecutive[bis] <= r - 1):
            return (ze // 3) + (on // 3)

        return 1 + (ze // 3) + (on // 3)

    for _ in range(q):
        print(query())

for c in range(cases):
    solve()

