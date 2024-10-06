# https://stackoverflow.com/a/568618/14853184
def gen_primes():
  D = {}
  q = 2
  while True:
    if q not in D:
      yield q
      D[q * q] = [q]
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      del D[q]
    q += 1

def solve():
  n = int(input())

  if n <= 4:
    return 0

  res = 0
  last = 0

  gen = gen_primes()

  while True:
    num = next(gen)
    if num > n:
      break

    if num - last == 2:
      res += 1

    last = num

  return res

cases = int(input())
for i in range(cases):
  print(f"Case #{i+1}: {solve()}")
