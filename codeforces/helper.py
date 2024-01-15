from random import randint

BOUND_MIN = 1
BOUND_MAX = 10**9

N = 10
# N = 10**5

print(range(N))
for _ in N:
  print(randint(BOUND_MIN, BOUND_MAX), end=" ")
print()
