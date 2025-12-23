from math import lcm, gcd

cases = int(input())

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    assert n == len(nums)
    nums.sort()
    return max(nums[0], nums[1]-nums[0])

for c in range(cases):
    print(solve())
