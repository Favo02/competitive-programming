import sys
from collections import defaultdict

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
seen = {}
cycle_detected = False
coins_for_time = []

res = 0

time = 0
TIME = 202420242024
while time < TIME:

  index = tuple((cur + spins[i]) % len(cats[i]) for i, cur in enumerate(index))

  if not cycle_detected and index in seen:
    cycle_start = seen[index]
    cycle_size = time - cycle_start
    cycles = (TIME - time) // cycle_size

    cycle_coins = 0
    for t in range(cycle_start, time):
      cycle_coins += coins_for_time[t]

    res += cycles * cycle_coins
    time += cycles * cycle_size
    cycle_detected = True

  seen[index] = time
  coins_for_time.append(coins(index))
  res += coins_for_time[-1]
  time += 1

print(res)
