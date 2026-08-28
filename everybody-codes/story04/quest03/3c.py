w = int(input().strip().split("=")[1])
h = int(input().strip().split("=")[1])

ho = input().strip().split("=")[1]
vo = input().strip().split("=")[1]

ww = len(vo) * 2
hh = len(ho) * 2

colors = {}
walls = 0
for x in range(ww):
    for y in range(hh):
        if y == 0:
            colors[(x, y)] = walls % 2
            walls += (1 + y + int(vo[(x + 1) % len(vo)])) % 2
        else:
            colors[(x, y)] = (
                colors[(x, y - 1)] + ((1 + x + int(ho[y % len(ho)])) % 2)
            ) % 2
        # print(x, y, colors[(x, y)])

res = [0, 0]
for x in range(ww):
    for y in range(hh):
        left = (1 + y + int(vo[x % len(vo)])) % 2
        right = (1 + y + int(vo[(x + 1) % len(vo)])) % 2
        top = (1 + x + int(ho[y % len(ho)])) % 2
        bottom = (1 + x + int(ho[(y + 1) % len(ho)])) % 2

        if left + right + top + bottom == 4:
            # print(x, y, colors[(x, y)])
            res[colors[(x, y)]] += 1

wblocks = w // ww
hblocks = h // hh
blocks = wblocks * hblocks
res[0] *= blocks
res[1] *= blocks

remx = w - (ww * wblocks)
remy = h - (hh * hblocks)

vertband = [0, 0]
for x in range(remx):
    for y in range(hh):
        left = (1 + y + int(vo[x % len(vo)])) % 2
        right = (1 + y + int(vo[(x + 1) % len(vo)])) % 2
        top = (1 + x + int(ho[y % len(ho)])) % 2
        bottom = (1 + x + int(ho[(y + 1) % len(ho)])) % 2

        if left + right + top + bottom == 4:
            # print(x, y, colors[(x, y)])
            vertband[colors[(x, y)]] += 1
vertband[0] *= hblocks
vertband[1] *= hblocks

horband = [0, 0]
for x in range(ww):
    for y in range(remy):
        left = (1 + y + int(vo[x % len(vo)])) % 2
        right = (1 + y + int(vo[(x + 1) % len(vo)])) % 2
        top = (1 + x + int(ho[y % len(ho)])) % 2
        bottom = (1 + x + int(ho[(y + 1) % len(ho)])) % 2

        if left + right + top + bottom == 4:
            # print(x, y, colors[(x, y)])
            horband[colors[(x, y)]] += 1
horband[0] *= wblocks
horband[1] *= wblocks

for x in range(remx):
    for y in range(remy):
        left = (1 + y + int(vo[x % len(vo)])) % 2
        right = (1 + y + int(vo[(x + 1) % len(vo)])) % 2
        top = (1 + x + int(ho[y % len(ho)])) % 2
        bottom = (1 + x + int(ho[(y + 1) % len(ho)])) % 2

        if left + right + top + bottom == 4:
            # print(x, y, colors[(x, y)])
            res[colors[(x, y)]] += 1

res[0] += horband[0] + vertband[0]
res[1] += horband[1] + vertband[1]
# print(blocks)

# print(res)
print(max(res))
