import sys

tracks, swaps, test = map(lambda lines: lines.split("\n"), sys.stdin.read().strip().split("\n\n"))

for s in swaps:
  a, b = map(int, s.split("-"))
  blocklen = min(abs(b-a), len(tracks)-b+1, len(tracks)-a+1)
  a -= 1
  b -= 1
  tracks[a:a+blocklen], tracks[b:b+blocklen] = tracks[b:b+blocklen], tracks[a:a+blocklen]

print(tracks[int(test[0])-1])
