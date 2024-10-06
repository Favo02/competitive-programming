from math import sqrt

n, s, t = map(int, input().split())
segm = []
points = []
res = 0

for i in range(n):
  sx, sy, ex, ey = map(int, input().split())
  segm.append((sx, sy, ex, ey))
  points.append((i, sx, sy, ex, ey))
  points.append((i, ex, ey, sx, sy))

def dist(cx, cy, dx, dy):
  return sqrt((cx-dx)**2 + (cy-dy)**2)

def solve(cx, cy, done):
  if len(done) == n:
    return 0

  res = float('inf')
  for (i, sx, sy, ex, ey) in points:
    if i in done:
      continue
    res = min(res, (dist(cx, cy, sx, sy)/s) + (dist(sx, sy, ex, ey)/t) + solve(ex, ey, done | {i}))

  return res

print(solve(0, 0, set()))
