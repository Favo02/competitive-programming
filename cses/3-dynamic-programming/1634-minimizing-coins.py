
def solve():
  n, x = map(int, input().split())
  coins = list(map(int, input().split()))
  INF = x+1

  assert len(coins) == n

  dp = [INF] * x

  for c in coins:
    if c == x:
      return 1
    if c < x:
      dp[c-1] = 1

  for i in range(x):
    if dp[i] != INF:
      for c in coins:
        if i + c < x:
          dp[i+c] = min(dp[i+c], dp[i] + 1)

  return -1 if dp[-1] == INF else dp[-1]

print(solve())
