import sys

ev = {}

for line in sys.stdin:
  fromm, to = line.strip().split(":")
  ev[fromm] = to.split(",")

therm = ["A"]

for day in range(4):
  newtherm = []
  for t in therm:
    newtherm.extend(ev[t])
  therm = newtherm

print(len(therm))
