string = input().strip()
valid = (s for s in string if ('a' <= s <= 'z') or ('A' <= s <= 'Z'))
res = 0
for s in valid:
  if 'a' <= s <= 'z':
    res += ord(s) - ord('a') + 1
  if 'A' <= s <= 'Z':
    res += ord(s) - ord('A') + 27
print(res)
