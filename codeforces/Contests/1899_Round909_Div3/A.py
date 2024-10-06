import sys

cases = input()

lines = []
for l in sys.stdin:
  n = int(l.rstrip('\n'))

  if (n+1) % 3 == 0 or (n-1) % 3 == 0:
    print("First")
  else:
    print("Second")
