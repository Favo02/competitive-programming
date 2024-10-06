def valid(string, base, LEN):
  # print("base:", base)
  length = len(base)
  diff = 0

  for start in range(0, len(string), length):
    if diff > 1: break
    for i in range(length):
      if start+i >= LEN or i >= LEN or string[start+i] != base[i]:
        diff += 1
      if diff > 1: break

  if diff <= 1:
    return True, length
  return False, 0



def solve():
  LEN = int(input())
  string = input()


  for length in range(1, LEN):
    if LEN % length != 0: continue

    base1 = string[:length]
    base2 = string[length:length*2]


    val, res = valid(string, base1, LEN)
    if val:
      return res
    val, res = valid(string, base2, LEN)
    if val:
      return res

  return LEN

cases = int(input())

for _ in range(cases):
  print(solve())
