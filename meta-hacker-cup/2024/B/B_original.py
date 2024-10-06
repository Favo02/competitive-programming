import sys

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

  gen = gen_primes()
  primes = []
  # seen = {2}
  res = 1

  while True:
    num = next(gen)
    if num <= n:
      primes.append(num)
    else:
      break

    # for p in primes:
    #   if (num - p) in primes:
    #     seen.add(num - p)

  for a, b in zip(primes, primes[1:]):
    if b-a == 2:
      # seen.add(a)
      res += 1

  # print(len(primes))
  # assert len(seen) == res
  return res

cases = int(input())
for i in range(cases):
  print(i, file=sys.stderr)
  print(f"Case #{i+1}: {solve()}")
