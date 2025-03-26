import sys

balances, transactions = sys.stdin.read().strip().split("\n\n")

bal = {}

for b in balances.splitlines():
  who, num = b.split(" HAS ")
  bal[who] = int(num)

for t in transactions.splitlines():
  tokens = t.split()
  fromm, to, amt = tokens[1], tokens[3], tokens[5]
  bal[fromm] -= int(amt)
  bal[to] += int(amt)

print(sum(sorted(bal.values())[-3:]))
