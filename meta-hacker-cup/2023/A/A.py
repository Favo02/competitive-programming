def parseInput():
  input = open("in.txt", "r")
  input = open("fullinput.txt", "r")
  # input = open("small.txt", "r")
  lines = []
  for i, line in enumerate(input):
    if i == 0: continue
    if i % 2 != 0: continue
    line = line.split("\n")[0]
    line = line.split(" ")
    lines.append(line)
  return lines

lines = parseInput()
# print(lines)

for i, elfs in enumerate(lines):
  elfs = list(map(lambda e : int(e), elfs))
  elfs.sort()

  if len(elfs) != 5:
    start = (elfs[0] + elfs[1]) / 2
    end = (elfs[-2] + elfs[-1]) / 2
    res = end-start

  else:
    start = (elfs[0] + elfs[2]) / 2
    end = (elfs[-2] + elfs[-1]) / 2
    res1 = end-start

    start = (elfs[0] + elfs[1]) / 2
    end = (elfs[-3] + elfs[-1]) / 2
    res2 = end-start
    
    res = max(res1, res2)

  if res.is_integer():
    print("Case #", i+1, ": ", int(res), sep="")
  else:
    print("Case #", i+1, ": ", res, sep="")
