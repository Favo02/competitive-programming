nk = input().split(" ")
n,k = int(nk[0]), int(nk[1])

meetings = []
for i in range(n):
  m = input().split(" ")
  meetings.append((int(m[0]), int(m[1])))


def calcolaMeetings(meetings):
  meetings.sort(key=lambda x : x[1])
  meetings.sort(key=lambda x : x[0])
  #print(meetings)

  open = []
  count = 0
  Max = []
  for s,e in meetings:
    count = 0
    open.append(e)
    #print(f"open: {open}")
    for s2, _ in meetings:
      if s2 >= s and s2 <= e:
        count += 1

    Max.append(count)
  return Max

while(k != -1):
  Max = calcolaMeetings(meetings)
  index = Max.index(max(Max))
  del meetings[index]
  k -= 1

  #print(f"Max: {Max} k: {k}")

print(max(Max))


"""
dict = {}
for m in Max:
  if m in dict:
    dict[m] += 1
  else:
    dict[m] = 1

print(dict)

res = 0
for t,v in dict.items():
  #print(t, v, t-math.ceil(k/v))
  res = max(res, t-math.ceil(k/v))
"""

#print(Max)
#print(res)
# print(Max-k)

