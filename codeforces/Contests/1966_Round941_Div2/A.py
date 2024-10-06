from collections import Counter

def solve():
  l, k = [int(n) for n in input().split()]
  cards = [int(n) for n in input().split()]
  cards = Counter(cards)

  for c, qty in cards.items():
    if qty >= k:
      return k-1

  return l

cases = int(input())
for _ in range(cases):
  print(solve())
