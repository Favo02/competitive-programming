from collections import deque

def solve():
  l = int(input())
  piles = [int(n) for n in input().split()]
  assert l == len(piles)
  piles = list(set(piles))

  if len(piles) == 1:
    return "Alice"

  piles.sort()
  piles = piles[:-1]

  diff = [ piles[0] ] + [b-a for a,b in zip(piles, piles[1:])]

  count = 0
  ones = deque()
  for d in reversed(diff):
    ones.appendleft(count)
    if d == 1:
      count += 1
    else:
      count = 0

  # print("diff", diff)
  # print("ones", list(ones))

  winner = True
  for i, d in enumerate(diff):
    if d == 1:
      winner = not winner
      continue

    if ones[i] % 2 == 1:
      winner = not winner

  return "Alice" if winner else "Bob"

cases = int(input())
for _ in range(cases):
  # print()
  print(solve())
