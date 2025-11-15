n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    dist = [-1 if a < 0 else (1 if a > 0 else 0) for a in nums]
    nums = [1 if a == 0 else abs(a) for a in nums]
    print(sum(dist), sum(nums))
