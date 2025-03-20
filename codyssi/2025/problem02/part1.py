import sys

def parseop(string):
  n = int(string.split()[-1])
  if string.startswith("ADD "):
    return lambda x: x + n
  if string.startswith("MULTIPLY "):
    return lambda x: x * n
  if string.startswith("RAISE TO THE POWER OF "):
    return lambda x: x ** n

lines = list(map(str.strip, sys.stdin.readlines()))

ops = [parseop(l.split(": ")[1]) for l in lines[:3]]

nums = sorted(int(n) for n in lines[4:])
med = nums[len(nums)//2]

for op in reversed(ops):
  med = op(med)
print(med)
