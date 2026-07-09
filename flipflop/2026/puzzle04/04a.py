import sys

lines = sys.stdin.readlines()
# cut = lines[:-9]
cut = lines[:-401]

print("".join(cut).count('o'))
