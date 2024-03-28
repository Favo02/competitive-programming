cases = int(input())

for _ in range(cases):

  LEN = int(input())

  even = []
  odd = []

  for i in range(LEN):
    if i % 2 == 0:
      even.append("##")
      odd.append("..")
    else:
      odd.append("##")
      even.append("..")

  e = "".join(even)
  o = "".join(odd)

  for r in range(LEN):
    if r % 2 == 0:
      print(e)
      print(e)
    else:
      print(o)
      print(o)
