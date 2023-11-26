import sys

def countOcc(str):
  res = {}
  for s in str:
    if s in res:
      res[s] += 1
    else:
      res[s] = 1
  return res

lines = []
for l in sys.stdin:
  lines.append(l[:-1])

lines = lines[1:]
# print(lines)

for i in range(0, len(lines), 2):
  k = int(lines[i].split(" ")[1])
  str = lines[i+1]
  # print(k, str)
  occ = countOcc(str)
  # print(occ)

  newL = len(str) - k
  res = None
  if newL % 2 == 0:
    for c,key in occ.items():
      if key % 2 != 0:
        k -= 1
    res = k >= 0 and k % 2 == 0
  else:
    even = 0
    odd = 0
    for c,key in occ.items():
      if key % 2 == 0:
        even +=1
      else:
        odd += 1
    k -= (odd-1)
    res = k>= 0 and k %2 == 0

  print("YES" if res else "NO")


