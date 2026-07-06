import sys

print(sum(map(lambda l: max(0, 60 - int(l.strip())), sys.stdin.readlines())))
