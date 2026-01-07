def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    assert n == len(nums)
    if nums[-1] == nums[0] == 0:
        return "Bob"
    return "Alice"

cases = int(input())
for _ in range(cases):
    print(solve())
