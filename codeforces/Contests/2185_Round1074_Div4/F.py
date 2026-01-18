def solve():
    n, q = map(int, input().split())
    cows = list(map(int, input().split()))
    assert len(cows) == 2**n

    tree = [cows.copy()]
    for _ in range(n):
        tree.append([tree[-1][i] ^ tree[-1][i+1] for i in range(0, len(tree[-1]), 2)])

    # print("\n".join(map(str, reversed(tree))), "\n")

    def simulate(b, c):
        res = 0
        size = 1
        row = 0
        while row < len(tree)-1:
            # print(tree[row])
            if b % 2 == 0:
                if tree[row][b+1] > c:
                    res += size
                c ^= tree[row][b+1]
            else:
                if tree[row][b-1] >= c:
                    res += size
                c ^= tree[row][b-1]

            row += 1
            b //= 2
            size *= 2
        return res

    for _ in range(q):
        b, c = map(int, input().split())
        # print(b-1)
        print(simulate(b-1, c))
        # print()

cases = int(input())

for _ in range(cases):
    solve()
