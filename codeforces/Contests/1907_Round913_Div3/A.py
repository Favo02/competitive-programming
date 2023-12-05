cases = int(input())

rows = ['a','b','c','d','e','f','g','h']
cols = [1,2,3,4,5,6,7,8]

while cases > 0:
  cases -= 1
  pos = input()

  for r in rows:
    if f"{r}{pos[1]}" != pos:
      print(f"{r}{pos[1]}")
  for c in cols:
    if f"{pos[0]}{c}" != pos:
      print(f"{pos[0]}{c}")

