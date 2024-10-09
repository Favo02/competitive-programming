MOD = 10**9 + 7

n, x = map(int, input().split())
coins = list(filter(lambda c: c <= x, map(int, input().split())))

dp = [0] * x

for c in coins:
  dp[c-1] = 1

for i, count in enumerate(dp):
  if count == 0:
    continue

  for c in coins:
    if i+c < x:
      dp[i+c] = (dp[i+c] + count) % MOD

print(dp[-1])
