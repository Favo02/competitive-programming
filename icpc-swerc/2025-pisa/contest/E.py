n, q = map(int, input().split())
s = input()

quattro = [0]
otto = [0]

for ss in s:
    if ss == '4':
        quattro.append(quattro[-1] + 1)
    else:
        quattro.append(quattro[-1])
    if ss == '8':
        otto.append(otto[-1] + 1)
    else:
        otto.append(otto[-1])

def check(qu, ot, x, y):
    x = abs(x)
    y = abs(y)

    x = max(0, x - ot)
    y = max(0, y - ot)

    if qu >= x + y:
        return True
    return False

for _ in range(q):
    l, r, x, y = map(int, input().split())

    qu = quattro[r] - quattro[l-1]
    ot = otto[r] - otto[l-1]

    if check(qu, ot, x, y):
        print("YES")
    else:
        print("NO")
