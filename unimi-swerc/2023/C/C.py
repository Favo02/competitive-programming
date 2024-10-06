from numpy import ones,vstack
from numpy.linalg import lstsq

# from https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
def line_intersection(line1, line2):
  xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
  ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

  print(xdiff, ydiff)

  def det(a, b):
      return a[0] * b[1] - a[1] * b[0]

  div = det(xdiff, ydiff)
  if div == 0:
      raise Exception('lines do not intersect')

  d = (det(*line1), det(*line2))
  x = det(d, xdiff) / div
  y = det(d, ydiff) / div
  return x, y


tokens = [int(n) for n in input().split(" ")]
x1, y1, x2, y2 = tokens[0], tokens[1], tokens[2], tokens[3]

xx1, xx2, yy1, yy2 = 0,0,0,0

if x1 == x2:
  print(x1)
elif x1 < x2:
  xx1 = x1+1
  yy1 = y1-1

  xx2 = x2-1
  yy2 = y2-1

else:
  xx1 = x1-1
  yy1 = y1-1

  xx2 = x2+1
  yy2 = y2-1

print(x1, y1, x2, y2)
print(xx1, yy1)
print(xx2, yy1)

A = (x1,y1)
B = (xx1,yy1)
C = (x2,y2)
D = (xx2,yy2)

print(A, B)
print(C, D)

print(line_intersection((A, B), (C, D)))
