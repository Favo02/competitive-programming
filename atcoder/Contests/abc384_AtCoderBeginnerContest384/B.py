N, R = map(int, input().split())
for _ in range(N):
  d, a = map(int, input().split())
  if d == 1: # 1600 - 2799
    if 1600 <= R <= 2799:
      R += a

  if d == 2: # 1200 - 2399
    if 1200 <= R <= 2399:
      R += a

print(R)
