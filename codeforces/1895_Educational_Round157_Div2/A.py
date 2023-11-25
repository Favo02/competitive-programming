import sys

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

for l in lines[1:]:
  tokens = l.split(" ")
  chest = int(tokens[0])
  key = int(tokens[1])
  stamina = int(tokens[2])
  # print(chest, key, stamina)
  if chest > key:
    print(chest)
  else:
    minus = (key-chest-stamina)  if (key-chest-stamina) > 0 else 0
    print(key + minus)
