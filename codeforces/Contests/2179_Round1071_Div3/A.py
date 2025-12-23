cases = int(input())

def solve():
    k, x = map(int, input().split())
    if k == 1:
        return x+1

    used = 0
    for i in range(1+x, 1000, x):
        used += 1
        if used == k-1:
            return i+x


    # print(n, x)

for c in range(cases):
    print(solve())
