from collections import deque
import sys

def isother(c):
  return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == '-'

def reduce(line):
  stack = deque()
  for l in line:
    if l.isdigit() and stack and isother(stack[-1]) or isother(l) and stack and stack[-1].isdigit():
      stack.pop()
    else:
      stack.append(l)
  return "".join(stack)

lines = sys.stdin.read().strip().splitlines()

res = 0
for line in lines:
  res += len(reduce(line))
print(res)
