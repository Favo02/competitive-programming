import sys
from collections import defaultdict, deque

balances, transactions = sys.stdin.read().strip().split("\n\n")

bal = {}
debts = defaultdict(deque)

def tran(fromm, to, amt):
  newamt = min(amt, bal[fromm])

  if newamt < amt:
    debts[fromm].append((to, amt-newamt))

  amt = newamt
  bal[fromm] -= amt
  bal[to] += amt

  while debts[to]:
    dto, damt = debts[to].popleft()
    if damt > bal[to]:
      debts[to].appendleft((dto, damt-bal[to]))
    tran(to, dto, min(damt, bal[to]))
    if bal[to] == 0:
      break

for b in balances.splitlines():
  who, num = b.split(" HAS ")
  bal[who] = int(num)

for t in transactions.splitlines():
  tokens = t.split()
  fromm, to, amt = tokens[1], tokens[3], tokens[5]
  amt = int(amt)
  tran(fromm, to, amt)

print(sum(sorted(bal.values())[-3:]))
