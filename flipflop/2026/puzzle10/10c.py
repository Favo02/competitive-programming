import sys
lines = list(map(str.strip, sys.stdin.readlines()))

labels = {}
MOD = 65536
compiled = []

def load(val, dest_reg):
    regs[dest_reg] = val
def copy(src_reg, dest_reg):
    regs[dest_reg] = regs[src_reg]
def add(src_reg1, src_reg2, dest_reg):
    regs[dest_reg] = (regs[src_reg1] + regs[src_reg2]) % MOD
def sub(src_reg1, src_reg2, dest_reg):
    regs[dest_reg] = (regs[src_reg1] - regs[src_reg2]) % MOD
def mul(src_reg1, src_reg2, dest_reg):
    regs[dest_reg] = (regs[src_reg1] * regs[src_reg2]) % MOD
def mod(src_reg1, src_reg2, dest_reg):
    if regs[src_reg2] == 0:
        regs[dest_reg] = 0
    else:
        regs[dest_reg] = regs[src_reg1] % regs[src_reg2]
def inc(reg):
    regs[reg] = (regs[reg] + 1) % MOD
def dec(reg):
    regs[reg] = (regs[reg] - 1) % MOD
def jump(label):
    global instruction
    instruction = labels[label]
def jz(reg, label):
    if regs[reg] == 0:
        jump(label)
def jnz(reg, label):
    if regs[reg] != 0:
        jump(label)
ops = [load, copy, add, sub, mul, mod, inc, dec, jump, jz, jnz]

for i, l in enumerate(lines):
    if l[:2] == "ba":
        tokens = l[2:].split("ne")
        iid, *args = list(map(lambda v: len(v)//2, tokens))
        compiled.append((ops[iid], args))
    if l[:2] == "be":
        lid = (len(l) - 2)//2
        labels[lid] = i
        compiled.append((lambda x: 0, (0,)))

res = 0
for r0 in range(0, 16):
    for r1 in range(0, 16):
        regs = [0] * 16
        regs[0] = r0
        regs[1] = r1
        instruction = 0
        steps = 0

        while instruction < len(lines):
            if steps >= 5000000:
                res += 1
                break
            op, args = compiled[instruction]
            op(*args)
            instruction += 1
            steps += 1

print(res * (MOD//16))
