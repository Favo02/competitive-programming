from heapq import heappop, heappush

def solve():
    N = int(input())
    nums = list(map(lambda s: int(s)-1, input().split()))
    assert N == len(nums)

    heap = []

    super = 0
    res = 0
    for i in range(N):
        if nums[i] > i:
            heappush(heap, nums[i])
        if nums[i] <= i:
            super += 1
        while heap and heap[0] <= i:
            heappop(heap)
        res = max(res, len(heap) + super)

    print(res)

t = int(input())
for _ in range(t):
    solve()
