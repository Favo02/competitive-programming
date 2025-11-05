import sys
names, instr = map(lambda l: l.split(","), sys.stdin.read().split("\n\n"))

for inst in instr:
    dir, qty = inst[0], inst[1:]
    qty = (1 if dir == "R" else -1) * (int(qty) % len(names))

    names[0], names[qty] = names[qty], names[0]

print(names[0])
