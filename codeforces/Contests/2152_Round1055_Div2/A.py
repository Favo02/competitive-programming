cases = int(input())

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == n
    unique = set(nums)
    return 2*len(unique) - 1

for c in range(cases):
    print(solve())
