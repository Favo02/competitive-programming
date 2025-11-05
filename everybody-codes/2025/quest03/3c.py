from collections import Counter

nums = list(map(int, input().split(",")))
c = Counter(nums)

print(max(c.values()))
