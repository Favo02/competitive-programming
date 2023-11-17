import sys

cases = int(input())

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

for i in range(0, len(lines), 2):
  boxes = int(lines[i])
  weigths = [int(w) for w in lines[i+1].split(" ")]

  # print(boxes, weigths)
  diff = 0
  for k in range(1, boxes):
    if boxes % k == 0:
      maxx = 0
      minn = 10**99

      # print(k)
      for i in range(0, len(weigths), k):
        nd = sum(weigths[i:i+k])
        maxx = max(maxx, nd)
        minn = min(minn, nd)

      # print(k, maxx, minn)
      diff = max(diff, (maxx - minn))

  print(diff)
