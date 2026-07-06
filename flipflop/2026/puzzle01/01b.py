import sys

print(sum(map(lambda l: max(max(0, 60 - int(l.strip())), 5*max(0, int(l.strip()) - 60)), sys.stdin.readlines())))
