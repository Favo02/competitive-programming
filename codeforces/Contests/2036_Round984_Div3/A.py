
def solve():
  n = int(input())

  notes = list(map(int, input().split()))
  assert len(notes) == n

  diff = [abs(a-b) for a, b in zip(notes, notes[1:])]

  for d in diff:
    if d != 5 and d != 7:
      print("NO")
      break
  else:
    print("YES")

c = int(input())
for _ in range(c):
  solve()
