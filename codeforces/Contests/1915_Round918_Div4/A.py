from collections import Counter

cases = int(input())

for _ in range(cases):
  nums = Counter(input().split())
  for n,v in nums.items():
    if v == 1:
      print(n)
