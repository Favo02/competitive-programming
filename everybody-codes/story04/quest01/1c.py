import sys

lines = sys.stdin.readlines()

res = 0
for line in lines:
    nums = [int(n) for n in line.strip().split(",")]
    below = []
    above = []

    seen = set()
    cur = 0

    flip = True
    for j in nums:
        # print(above)
        # print(below)
        # print(cur, j)

        back = False
        if (cur - j) > 0 and (cur - j) not in seen:
            nextt = cur - j
            back = True
            c, d = min(cur, nextt), max(cur, nextt)
            for a, b in below if flip else above:
                if (c < a < d and not (c < b < d)) or (c < b < d and not (c < a < d)):
                    back = False
                    break
            if back:
                if flip:
                    below.append((min(cur, nextt), max(cur, nextt)))
                else:
                    above.append((min(cur, nextt), max(cur, nextt)))

                cur = nextt

        if not back:
            # print("not back")
            nextt = cur + j
            stop = False
            while not stop:
                # print(nextt)
                valid = True
                if nextt in seen:
                    # print("invalid seen")
                    valid = False
                    nextt += 1
                    continue

                c, d = min(cur, nextt), max(cur, nextt)

                for a, b in below if flip else above:
                    # print(a, b, c, d)
                    if c < a < d and not (c < b < d):
                        # print("invalid cab")
                        valid = False
                        nextt += 1
                        break
                    if c < b < d and not (c < a < d):
                        # print("invalid cdb")
                        valid = False
                        stop = True
                        flip = not flip
                        break
                if stop:
                    break
                if valid:
                    if flip:
                        below.append((min(cur, nextt), max(cur, nextt)))
                    else:
                        above.append((min(cur, nextt), max(cur, nextt)))
                    cur = nextt
                    break
        flip = not flip
        seen.add(cur)
    # print("----------------", cur)
    res += cur
print(res)
