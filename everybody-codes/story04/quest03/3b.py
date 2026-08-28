w = int(input().strip().split("=")[1])
h = int(input().strip().split("=")[1])

ho = input().strip().split("=")[1]
vo = input().strip().split("=")[1]

colors = {}
walls = 0
for y in range(h):
    for x in range(w):
        if y == 0:
            colors[(x, y)] = walls % 2
            walls += (1 + y + int(vo[(x + 1) % len(vo)])) % 2
        else:
            colors[(x, y)] = (
                colors[(x, y - 1)] + ((1 + x + int(ho[y % len(ho)])) % 2)
            ) % 2
        # print(x, y, colors[(x, y)])

res = [0, 0]
for x in range(w):
    for y in range(h):
        left = (1 + y + int(vo[x % len(vo)])) % 2
        right = (1 + y + int(vo[(x + 1) % len(vo)])) % 2
        top = (1 + x + int(ho[y % len(ho)])) % 2
        bottom = (1 + x + int(ho[(y + 1) % len(ho)])) % 2

        if left + right + top + bottom == 4:
            # print(x, y, colors[(x, y)])
            res[colors[(x, y)]] += 1
print(max(res))
