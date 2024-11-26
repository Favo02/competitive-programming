import sys
from collections import defaultdict
from functools import lru_cache

sys.setrecursionlimit(10**6)

def coins(seq):
  count = defaultdict(int)
  for i, ind in enumerate(seq):
    for ic, char in enumerate(cats[i][ind]):
      if ic == 1: continue
      count[char] += 1

  res = 0
  for v in count.values():
    if v >= 3: res += v-2
  return res

@lru_cache(None)
def solve(seq, TIME, time):
  if time == TIME:
    return 0, 0

  # back
  back = tuple((cur - 1 + spins[i]) % len(cats[i]) for i, cur in enumerate(seq))
  cback = coins(back)
  bmin, bmax = solve(back, TIME, time+1)
  bmin, bmax = bmin + cback, bmax + cback

  # forward
  forw = tuple((cur + 1 + spins[i]) % len(cats[i]) for i, cur in enumerate(seq))
  cforw = coins(forw)
  fmin, fmax = solve(forw, TIME, time+1)
  fmin, fmax = fmin + cforw, fmax + cforw

  # nothing
  noth = tuple((cur + spins[i]) % len(cats[i]) for i, cur in enumerate(seq))
  cnoth = coins(noth)
  nmin, nmax = solve(noth, TIME, time+1)
  nmin, nmax = nmin + cnoth, nmax + cnoth

  return min(bmin, fmin, nmin), max(bmax, fmax, nmax)

spins = list(map(int, input().split(",")))
input()

N = len(spins)

cats = [[] for _ in range(N)]
for line in sys.stdin:
  line = line.rstrip() # DO NOT STRIP LEFT
  for c in range(N):
    cat = line[4*c : 4*c + 3]
    if cat.strip():
      cats[c].append(cat)

index = [0] * N

TIME = 256
minn, maxx = solve(tuple(index), TIME, 0)
print(maxx, minn)
