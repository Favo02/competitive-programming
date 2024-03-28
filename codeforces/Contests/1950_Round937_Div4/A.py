cases = int(input())

for _ in range(cases):

  a,b,c = [int(n) for n in input().split()]
  # print(a,b,c)

  if a<b<c:
    print("STAIR")
  elif a<b>c:
    print("PEAK")
  else:
    print("NONE")
