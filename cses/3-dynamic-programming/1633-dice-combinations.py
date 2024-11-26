MOD = 10**9 + 7
n = int(input())

dp = [0] * (n+1)
dp[0] = 1

for i in range(n):

  for dice in range(1, 7):
    if i+dice > n:
      break

    dp[i+dice] = (dp[i+dice] + dp[i]) % MOD

print(dp[n])
