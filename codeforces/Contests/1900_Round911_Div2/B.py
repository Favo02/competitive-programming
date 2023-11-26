cases = int(input())

while cases > 0:
  cases -= 1
  line1 = input().split(" ")
  a,b,c = int(line1[0]),int(line1[1]), int(line1[2])

  resA, resB, resC = 0,0,0

  if (a==c): resB=1
  if (a==b): resC=1
  if (c==b): resA=1

  if ((a%2) == (c%2)) and ((max(a,c) - min(a,c)) <= b): resB = 1
  if ((a%2) == (b%2)) and ((max(a,b) - min(a,b)) <= c): resC = 1
  if ((c%2) == (b%2)) and ((max(c,b) - min(c,b)) <= a): resA = 1

  if (max(a,c)-min(a,c)) == (b + min(a,c)):
    if a<c: resA = 1
    if c<a: resC = 1

  if (max(a,b)-min(a,b)) == (c + min(a,b)):
    if b<a: resB = 1
    if a<b: resA = 1

  if (max(c,b)-min(c,b)) == (a + min(c,b)):
    if b<c: resB = 1
    if c<b: resC = 1

  print(resA,resB,resC)
