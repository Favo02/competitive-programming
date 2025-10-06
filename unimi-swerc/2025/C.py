n = int(input())

squads = []
for _ in range(n):
    a, b = map(int, input().split())
    squads.append((a, b))

squads.sort()

print(squads[-1][0] + squads[-1][1])
