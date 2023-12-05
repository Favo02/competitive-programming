cases = int(input())

while cases > 0:
  cases -= 1
  line = list(reversed(input()))

  res = []

  toSkipLower = 0

  toSkipUpper = 0

  for l in line:
    if l == 'b': toSkipLower += 1
    elif l == 'B': toSkipUpper += 1
    elif l.islower():
      if toSkipLower: toSkipLower -= 1
      else: res.append(l)
    else:
      if toSkipUpper: toSkipUpper -=1
      else: res.append(l)

  print("".join(reversed(res)))
