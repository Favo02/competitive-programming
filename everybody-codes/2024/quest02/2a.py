words = input()[6:].split(",")
input()

text = input()

res = 0
for i in range(0, len(text)):

  for w in words:
    if w == text[i:i+len(w)]:
      res += 1

print(res)
