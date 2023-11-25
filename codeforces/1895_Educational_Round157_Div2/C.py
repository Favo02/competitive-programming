import sys

def checkLuckyTicket(t):
  p1 = t[:len(t)//2]
  p2 = t[len(t)//2:]

  s1 = sum(p1)
  s2 = sum(p2)
  return s1 == s2

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

parts = lines[1].split(" ")
newP = []
for p in parts:
  newP.append([int(pp) for pp in p])
parts = newP
count = 0

for p1 in parts:
  for p2 in parts:
    if (len(p1) + len(p2)) % 2 != 0: continue
    if checkLuckyTicket(p1 + p2):
      count += 1

print(count)
