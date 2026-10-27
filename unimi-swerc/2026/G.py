from bisect import bisect_right

N, Q = map(int, input().split())
nums = sorted(map(int, input().split()))

for _ in range(Q):
    q = int(input())
    before = bisect_right(nums, q)
    if before == 0:
        print(q)
    else:
        while True:
            newbefore = bisect_right(nums, q + before)
            if newbefore == before:
                print(q + newbefore)
                break
            before = newbefore
