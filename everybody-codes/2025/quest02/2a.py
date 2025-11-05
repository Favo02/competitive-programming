A = list(map(int, input()[3:-1].split(",")))

def mul(a, b):
    X1, Y1 = a
    X2, Y2 = b
    return [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]

def div(a, b):
    X1, Y1 = a
    X2, Y2 = b
    return [X1 // X2, Y1 // Y2]

def sum(a, b):
    X1, Y1 = a
    X2, Y2 = b
    return [X1 + X2, Y1 + Y2]

res = [0,0]
for i in range(3):
    res = mul(res, res)
    res = div(res, [10, 10])
    res = sum(res, A)

print(res)

