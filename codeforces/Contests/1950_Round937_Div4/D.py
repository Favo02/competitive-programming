from functools import reduce

def isBin(n):
  while n > 0:
    if n % 10 != 0 and n % 10 != 1:
      return False
    n //= 10
  return True

# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python/
def factors(n):
  return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def solve(n):
  # print("=============", n)
  if isBin(n):
    return True

  while True:
    fact = factors(n)
    fact = {f for f in fact if f != 1 and f != n and isBin(f)}
    if len(fact) == 0:
      return False

    n //= max(fact)

    if isBin(n):
      return True

cases = int(input())
for _ in range(cases):
  res = solve(int(input()))
  if res:
    print("YES")
  else:
    print("NO")
