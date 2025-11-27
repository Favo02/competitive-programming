from functools import reduce

nums = list(map(int, input().split(",")))

spell = []
for i, n in enumerate(nums):
    cur = 0
    for a in spell:
        if (i+1) % a == 0:
            cur += 1
    assert n-1 <= cur <= n
    if cur == n-1:
        spell.append(i+1)

def needed(length):
    used = 0
    for s in spell:
        used += length // s
    return used

l = 1
r = 10000000000000000000000000000000

blocks = 202520252025000

while r-l >= 2:
    m = (r+l) // 2
    if needed(m) <= blocks:
        l = m
    else:
        r = m-1

if needed(r) <= blocks:
    print(r)
else:
    assert needed(l) <= blocks
    print(l)
