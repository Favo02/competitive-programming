from math import sqrt

N = 13195
N = 600851475143
isqrt = lambda n: int(sqrt(n))
res = max(n for n in range(2, isqrt(N)) if N % n == 0 and len([m for m in range(2, isqrt(n)+1) if n%m == 0]) == 0)

print(res)
