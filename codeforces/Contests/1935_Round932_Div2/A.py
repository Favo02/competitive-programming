cases = int(input())

for _ in range(cases):

  N = int(input())
  S = input()
  R = S[::-1]

  if R < S:
    if N % 2 == 1:
      print(R)
    else:
      print(R + S)
  else:
    if N % 2 == 1:
      print(S + R)
    else:
      print(S)
