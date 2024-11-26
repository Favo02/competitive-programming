import sys

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

PULLS = 100

index = [0] * N
for _ in range(PULLS):
  index = [(cur + spins[i]) % len(cats[i]) for i, cur in enumerate(index)]

print(" ".join([cats[i][ind] for i, ind in enumerate(index)]))

