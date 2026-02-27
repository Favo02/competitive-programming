def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == n
    if sorted(nums) == nums:
        return len(nums)
    return 1

for _ in range(int(input())):
    print(solve())
