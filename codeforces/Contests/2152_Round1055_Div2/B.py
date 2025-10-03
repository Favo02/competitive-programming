from collections import deque

cases = int(input())

DIRS = [
    ((0,1), (0,-1), (1,0), (-1,0)),
    ((0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1))
]

def solve():
    n, xR, yR, xC, yC = map(int, input().split())
    # print(n, xR, yR, xC, yC)

    ver = 0
    verDist = abs(yR-yC)
    if yR > yC:
        ver = n-yR
    elif yR < yC:
        ver = yR

    hor = 0
    horDist = abs(xR-xC)
    if xR > xC:
        hor = n-xR
    elif xR < xC:
        hor = xR

    return max(ver + verDist, hor + horDist)


for c in range(cases):
    print(solve())
