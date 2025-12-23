cases = int(input())

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == n
    # print(nums)
    deltas = []
    maxdelta = 0
    for i in range(n):
        if i == 0:
            deltas.append(abs(nums[0] - nums[1]))
        elif i == n-1:
            deltas.append(abs(nums[-1] - nums[-2]))
        else:
            deltas.append((abs(nums[i-1] - nums[i]) + abs(nums[i+1] - nums[i])) - abs(nums[i+1] - nums[i-1]))
        if deltas[i] > deltas[maxdelta]:
            maxdelta = i


    # print(deltas)
    nnnums = nums[:maxdelta] + nums[maxdelta+1:]
    # print(nnnums)
    return sum(abs(a-b) for a, b in zip(nnnums, nnnums[1:]))


for c in range(cases):
    print(solve())
    # print()
