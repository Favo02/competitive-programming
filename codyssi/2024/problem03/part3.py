import sys

summ = 0
lines = sys.stdin.read().strip().splitlines()

for l in lines:
  num, base = l.split()
  summ += int(num, int(base))

base65 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#"
res = []

while summ > 0:
  res.append(base65[summ % 65])
  summ //= 65

print("".join(reversed(res)))
