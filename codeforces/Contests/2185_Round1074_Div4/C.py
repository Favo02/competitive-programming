cases = int(input())

for _ in range(cases):
    n = int(input())
    nums = list(map(int, input().split()))
    assert n == len(nums)

    nums = list(set(nums))

    nums.sort()
    # print(nums)

    maxx = 0
    cur = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]+1:
            cur += 1
        else:
            maxx = max(maxx, cur)
            cur = 1
    maxx = max(maxx, cur)
    print(maxx)
