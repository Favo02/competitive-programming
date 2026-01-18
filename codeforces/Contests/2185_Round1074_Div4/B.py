cases = int(input())

for _ in range(cases):
    n = int(input())
    nums = list(map(int, input().split()))
    assert n == len(nums)
    print(n * max(nums))
