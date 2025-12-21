def check(get):
    ppp = [get(p) for p in points if get(p) != 0]
    if not ppp:
        return True
    fx = ppp[0] // abs(ppp[0])
    for p in ppp:
        if p // abs(p) != fx:
            return False
    return True

cases = int(input())
for _ in range(cases):
    p = int(input())
    points = []
    for _ in range(p):
        x, y = map(int, input().split())
        points.append((x, y))

    v = check(lambda p: p[0]) or check(lambda p: p[1])
    if (v):
        print("YES")
    else:
        print("NO")
