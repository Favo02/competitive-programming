words = input()[6:].split(",")
input()

res = 0

while True:
  try:
    line = input()
  except EOFError:
    break

  seen = set()

  for i in range(0, len(line)):
    for w in words:
      if w == line[i:i+len(w)]:
        # res += len(w)
        for sss in range(i, i+len(w)):
          seen.add(sss)

  for i in range(0, len(line)):
    for w in map(lambda ww: "".join(reversed(ww)), words):
      if w == line[i:i+len(w)]:
        # res += len(w)
        for sss in range(i, i+len(w)):
          seen.add(sss)

  res += len(seen)

print(res)
