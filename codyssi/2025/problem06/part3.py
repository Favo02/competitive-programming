string = input().strip()
res = 0

last = None
for s in string:
  if 'a' <= s <= 'z':
    val = ord(s) - ord('a') + 1
  elif 'A' <= s <= 'Z':
    val = ord(s) - ord('A') + 27
  else:
    while last < 1:
      last += 52
    while last > 52:
      last -= 52
    val = last

  res += val
  last = val * 2 - 5

print(res)
