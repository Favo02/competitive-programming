n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    nums.sort()
    print(sum(nn *- 1 for nn in nums[:-1]) + nums[-1])
