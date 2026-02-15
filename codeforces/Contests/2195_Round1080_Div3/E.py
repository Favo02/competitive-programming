import sys

sys.setrecursionlimit(10**6)
MOD = 10**9 + 7


def solve():
    n = int(input())

    parent = {}
    child = {}

    for i in range(n):
        a, b = map(int, input().split())
        if a == b == 0:
            continue
        child[i + 1] = (a, b)
        parent[a] = i + 1
        parent[b] = i + 1

    if n == 1:
        return 1

    undernodes = {}

    def bfs(cur):
        if cur not in child:
            undernodes[cur] = 0
            return 1
        a, b = child[cur]
        bfs(a)
        bfs(b)
        undernodes[cur] = 2 + undernodes[a] + undernodes[b]
        return undernodes[cur]

    bfs(1)

    res = {}

    def result(i):
        if i in parent:
            res[i] = (2 * undernodes[i] + 1 + res[parent[i]]) % MOD
        else:
            res[i] = (2 * undernodes[i] + 1) % MOD

        if i in child:
            a, b = child[i]
            result(a)
            result(b)

    result(1)

    return " ".join(map(lambda e: str(e[1]), sorted(res.items())))


for _ in range(int(input())):
    print(solve())
