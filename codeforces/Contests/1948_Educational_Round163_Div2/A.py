cases = int(input())

for _ in range(cases):
  N = int(input())

  if N == 0:
    print("AB")
    continue

  if N % 2 == 1:
    print("NO")
  else:
    print("YES")
    for i in range(N//2):
      # print(i)
      if i % 2 == 0:
        print("AA", end="")
      else:
        print("BB", end="")
    print()

