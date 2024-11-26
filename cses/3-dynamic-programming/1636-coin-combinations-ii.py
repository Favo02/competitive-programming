MOD = 10**9 + 7

n, x = map(int, input().split())
coins = list(filter(lambda c: c <= x, list(map(int, input().split()))))
coins.sort()

if len(coins) == 0:
  print(0)
  exit(0)

dp = [0] * x

for c in coins:
  dp[c-1] += 1

  for pos in range(x):
    if pos + c >= x:
      break
    dp[pos + c] = (dp[pos + c] + dp[pos]) % MOD

print(dp[-1])
