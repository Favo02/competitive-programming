MOD = 10**9 + 7

n = int(input())

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for row in range(n):
  for col, c in enumerate(input()):
    if c == "*":
      if row == col == 0:
        print(0)
        exit(0)
      continue

    up = left = 0
    if row != 0:
      up = dp[row-1][col]
    if col != 0:
      left = dp[row][col-1]

    dp[row][col] = (dp[row][col] + up + left) % MOD

print(dp[-1][-1])

