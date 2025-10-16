from functools import cache

X = input()
Y = int(input())

@cache
def solve(i, strict, used):
    if used > Y:
        return 0

    if i == len(X):
        if used == Y:
            return 1
        return 0

    res = 0
    upper = int(X[i]) if strict else 10
    for n in range(min(upper, 9), -1, -1):
        res += solve(i+1, n == upper, used + (n != 0))
    return res

print(solve(0, True, 0))
