def peaks():
  for half_length in range(1, 10):
    for start in range(1, 10-half_length+1):
      peak = []
      for i in range(start, start+half_length):
        peak.append(i)
      peak += peak[-2::-1]
      yield int("".join(map(str, peak)))

def solve(a, b, m):
  res = 0
  for pp in p:
    if a <= pp <= b:
      if pp % m == 0:
        res += 1
  return res

cases = int(input())
p = list(peaks())
for i in range(cases):
  a, b, mult = map(int, input().split())
  print(f"Case #{i+1}: {solve(a, b, mult)}")
