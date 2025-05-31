def case():
  N = int(input())
  S = input()
  assert len(S) == N

  # dp[OPEN/CLOSE][INTUSED][i]
  # dp[OPEN][USED] is useless, used/aval is only for CLOSE
  dp = [[[float("inf") for _ in range(N)] for _ in range(2)] for _ in range(2)]

  OPENN = 0
  CLOSE = 1

  AVAL = 0
  USED = 1

  if S[0] == "0":
    dp[CLOSE][AVAL][0] = 0
    dp[OPENN][AVAL][0] = 1
  else:
    dp[CLOSE][AVAL][0] = 1
    dp[OPENN][AVAL][0] = 0

  for i in range(1, len(S)):
    if S[i] == "0":
      dp[CLOSE][AVAL][i] = dp[CLOSE][AVAL][i-1]
      dp[CLOSE][USED][i] = min(dp[CLOSE][USED][i-1], dp[OPENN][AVAL][i-1])

      dp[OPENN][AVAL][i] = min(1 + dp[OPENN][AVAL][i-1], 1 + dp[CLOSE][AVAL][i-1])

    else:
      dp[CLOSE][AVAL][i] = 1 + dp[CLOSE][AVAL][i-1]
      dp[CLOSE][USED][i] = min(1 + dp[CLOSE][USED][i-1], 1 + dp[OPENN][AVAL][i-1])

      dp[OPENN][AVAL][i] = min(dp[OPENN][AVAL][i-1], dp[CLOSE][AVAL][i-1])

  res = float("inf")
  for oc in dp:
    for au in oc:
      res = min(au[-1], res)
  return res

C = int(input())
for _ in range(C):
  print(case())
