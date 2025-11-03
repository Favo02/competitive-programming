import sys
names, instr = map(lambda l: l.split(","), sys.stdin.read().split("\n\n"))

i = 0
for inst in instr:
    dir, qty = inst[0], inst[1:]
    qty = (1 if dir == "R" else -1) * int(qty)

    i = (i + qty) % len(names)

print(names[i])
