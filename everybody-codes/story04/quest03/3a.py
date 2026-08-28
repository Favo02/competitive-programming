w = int(input().strip().split("=")[1])
h = int(input().strip().split("=")[1])

ho = input().strip().split("=")[1]
vo = input().strip().split("=")[1]

res = 0

for x in range(w):
    for y in range(h):
        left = (1 + y + int(vo[x % len(vo)])) % 2
        right = (1 + y + int(vo[(x + 1) % len(vo)])) % 2
        top = (1 + x + int(ho[y % len(ho)])) % 2
        bottom = (1 + x + int(ho[(y + 1) % len(ho)])) % 2

        if left + right + top + bottom == 4:
            res += 1
        # print(x, y, left, right, top, bottom)
print(res)
