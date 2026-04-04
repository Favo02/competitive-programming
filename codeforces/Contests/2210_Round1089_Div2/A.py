def solve():
    n = int(input())
    for nn in range(n, 0, -1):
        print(nn, end=" ")
    print()

t = int(input())
for _ in range(t):
    solve()
