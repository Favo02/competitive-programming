cases = int(input())

events = []
while cases > 0:
  cases -= 1
  event = input().split(" ")
  events.append((int(event[0]), int(event[1])))

events.sort(key=lambda x: x[1])
time = {}
for e in events:
  if e[1] in time:
    time[e[1]].append(e[0])
  else:
    time[e[1]] = [e[0]]

events = []
for v in time.values():
  events.append(sum(v))

Max = 0
count = 0
for e in events:
  count += e
  Max = max(Max, count)

# print(events)
print(Max)
