import sys
import fractions

def toC(f):
  c = (f-32) * fractions.Fraction(5, 9)
  return c

input = []
for line in sys.stdin:
  l = line.split("/")
  f = fractions.Fraction(int(l[0]), int(l[1]))
  print(toC(f).numerator, "/", toC(f).denominator, sep="")
