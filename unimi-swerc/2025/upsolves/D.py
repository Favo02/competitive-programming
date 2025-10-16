from math import gcd

m, h = map(int, input().split())
nums = list(map(int, input().split()))

print(gcd(*(abs(m-h) for m in nums)))
