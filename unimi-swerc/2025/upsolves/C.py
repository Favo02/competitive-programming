n = int(input())

squad = (0, 0)
for _ in range(n):
    squad = max(squad, tuple(map(int, input().split())))

print(squad[0] + squad[1])
