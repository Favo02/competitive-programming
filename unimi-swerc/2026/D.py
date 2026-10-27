P = int(input())
portate = list(input().strip())
K = int(input())

swap = False
for _ in range(K):
    t, u, v = map(int, input().split())
    if t == 1:
        u -= 1
        v -= 1
        if swap:
            u = (u + P) % (2 * P)
            v = (v + P) % (2 * P)
        portate[u], portate[v] = portate[v], portate[u]
    if t == 2:
        swap = not swap

if swap:
    print("".join(portate[P:]), "".join(portate[:P]), sep="")
else:
    print("".join(portate))
