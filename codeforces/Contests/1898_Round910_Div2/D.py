def calcBeauty(a,b):
  beauty = []
  for i in range(L):
    beauty.append(abs(a[i] - b[i]))
  return beauty, sum(beauty)

cases = int(input())

while cases > 0:
  print()
  cases -= 1
  L = int(input())
  a = [int(n) for n in input().split(" ")]
  b = [int(n) for n in input().split(" ")]

  beauty, score = calcBeauty(a,b)

  print(score)

  beaMin = beauty.index(min(beauty))
  bMax = b.index(max(b))
  bMin = b.index(min(b))

  if abs(b[bMax] - b[beaMin]) > abs(b[bMin] - b[beaMin]):
    b[bMax], b[beaMin] = b[beaMin], b[bMax]
  else:
    b[bMin], b[beaMin] = b[beaMin], b[bMin]

  beauty, newScore = calcBeauty(a, b)
  print(newScore)
