cases = int(input())
for _ in range(cases):
    n = int(input())
    nums = list(map(float, input().split()))
    nums.sort()
    print(nums[-1] + nums[-2])
