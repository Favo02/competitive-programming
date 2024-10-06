def cmp(a, b):
  for aa, bb in zip(a,b):
    if aa == "?" or bb == "?":
      continue
    if aa != bb:
      return False
  return True

cases = int(input())

for _ in range(cases):
  string = input()
  res = 0

  for skip in range(0, len(string)):
    for length in range(2, len(string)+1 - skip, 2):

      L = len(string[skip:skip+length])
      if cmp((string[skip:skip+length])[:L//2], (string[skip:skip+length])[L//2:]):
        res = max(res, L)
  print(res)
