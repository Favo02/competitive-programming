# https://oeis.org/A002113
from math import log10, floor
def A002113(n):
  if n < 2: return 0
  P = 10**floor(log10(n//2)); M = 11*P
  s = str(n - (P if n < M else M-P))
  return int(s + s[-2 if n < M else -1::-1])

T = int(input())
for _ in range(T):
    N = int(input())
    rem = N % 12

    if str(N) == str(N)[::-1]:
        print(N, 0)

    elif rem == 0:
        print(0, N)

    elif rem != 10:
        print(rem, N - rem)

    else:

        i = 12
        while True:
            pal = A002113(i)
            i += 1
            if pal >= N:
                print(-1)
                break
            if ((N - pal) % 12) == 0:
                print(pal, N - pal)
                break
        else:
            print(-1)
