DIRS = [(-1,0), (+1,0), (0,-1), (0,+1)]

def dfs(sr, sc, word, wi, dr, dc):
  if wi == len(word):
    return True

  if not (0 <= sr < ROWS): return False

  sc = sc%COLS

  if word[wi] == text[sr][sc]:
    if dfs(sr+dr, sc+dc, word, wi+1, dr, dc):
      seen.add((sr, sc))
      return True
  else:
    return False

words = input()[6:].split(",")
input()

text = []
while True:
  try:
    line = input()
  except EOFError:
    break
  text.append(line)

ROWS = len(text)
COLS = len(text[0])
res = 0
seen = set()

for r, row in enumerate(text):
  for c, col in enumerate(row):
    for w in words:
      if col == w[0]:
        for dr, dc in DIRS:
          dfs(r, c, w, 0, dr, dc)

print(len(seen))
