from math import ceil

cases = int(input())

while cases > 0:
  cases -= 1

  segNum = int(input())
  segs = []

  t = input().split()
  ls, le = (int(t[0]), int(t[1]))

  maxx = 0
  for i in range(segNum-1):
    t = input().split()
    s, e = (int(t[0]), int(t[1]))

    dist = min(abs(e - ls), abs(s - le), abs(s - le), abs(s - ls))
    maxx = max(dist, maxx)

    ls, le = s, e
  print(maxx)
