from collections import Counter
from operator import itemgetter

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == n

    def sim(i, nums):
        while not all(n == 0 for n in nums):
            nums[i] = max(0, nums[i]-1)
            i = (i + 1) % n
        return i

    print(len(set(sim(i, nums.copy()) for i in range(n))))


for _ in range(int(input())):
    solve()
