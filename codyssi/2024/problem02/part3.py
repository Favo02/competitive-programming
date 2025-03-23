import sys

def solve(gates):
  if len(gates) == 0:
    return 0
  res = []
  count = 0
  for i, (a, b) in enumerate(zip(gates[::2], gates[1::2])):
    if ((i % 2 == 0) and (a and b)) or ((i % 2 == 1) and (a or b)):
      res.append(True)
      count += 1
    else:
      res.append(False)
  return count + solve(res)

gates = [l == "TRUE" for l in sys.stdin.read().strip().splitlines()]
res = len([g for g in gates if g]) + solve(gates)
print(res)
