import sys

dnas = list(map(lambda l: l.strip().split(":")[1], sys.stdin.readlines()))
print(sum(1 for a, b in zip(dnas[0], dnas[2]) if a == b) * sum(1 for a, b in zip(dnas[1], dnas[2]) if a == b))
