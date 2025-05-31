N, M = map(int, input().split())
turrets = []

diff = [0] * (N+1)


for _ in range(M):
  l, r = map(int, input().split())
  l -= 1
  r -= 1
  turrets.append((l, r))
  diff[l] += 1
  diff[r+1] -= 1

res = float("inf")
summ = 0
for i, d in enumerate(diff):
  summ += d
  # print(summ)
  if 0 <= i < N:
    res = min(summ, res)


# print(N, M)
# print(turrets)

# print(diff)

print(res)
