cases = int(input())

while cases > 0:
  cases -= 1
  input()
  cells = [len(s) for s in input().split("#") if len(s) > 0]
  # print(cells)

  res = 0
  for c in cells:
    if c >= 3:
      print(2)
      break
    if c > 1:
      res += 2
    else:
      res += 1
  else:
    print(res)

