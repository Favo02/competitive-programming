n, s = map(int, input().split())
taps = list(map(int, input().split()))

assert len(taps) == n

taps.insert(0, 0)

for a, b in zip(taps, taps[1:]):
  if b-a > s:
    print("No")
    break
else:
  print("Yes")
