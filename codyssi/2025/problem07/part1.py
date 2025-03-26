import sys

tracks, swaps, test = map(lambda lines: lines.split("\n"), sys.stdin.read().strip().split("\n\n"))

for s in swaps:
  a, b = map(int, s.split("-"))
  tracks[a-1], tracks[b-1] = tracks[b-1], tracks[a-1]

print(tracks[int(test[0])-1])
