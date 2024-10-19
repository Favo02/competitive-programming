n = int(input())

INF = float("inf")

nums = []
for _ in range(n):
  nums.append(int(input()))


minn = INF
res = 0

for i, n in enumerate(nums):
  if n < minn:
    minn = n
  elif n > minn:
    res = max(res, n - minn)

print(res)

