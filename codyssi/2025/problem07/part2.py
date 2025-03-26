import sys

tracks, swaps, test = map(lambda lines: lines.split("\n"), sys.stdin.read().strip().split("\n\n"))

for i, s in enumerate(swaps):
  a, b = map(int, s.split("-"))
  c = int(swaps[(i+1) % len(swaps)].split("-")[0])
  tracks[a-1], tracks[b-1], tracks[c-1] = tracks[c-1], tracks[a-1], tracks[b-1]

print(tracks[int(test[0])-1])
