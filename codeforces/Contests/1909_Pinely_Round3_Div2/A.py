cases = int(input())

while cases > 0:
  cases -= 1
  n = int(input())
  dirs = set()
  for _ in range(n):
    x,y = input().split()
    if int(x) > 0:
      dirs.add("U")
    elif int(x) < 0:
      dirs.add("D")
    if int(y) > 0:
      dirs.add("R")
    elif int(y) < 0:
      dirs.add("L")
  print("YES" if len(dirs) < 4 else "NO")
