cases = int(input())

while cases > 0:
  cases -= 1
  n = int(input())
  arr = [int(s) for s in input().split(" ")]
  # print(n, arr)

  Max = max(arr)
  Min = min(arr)
  count = 0
  ops = []

  while Max != Min and count < 10:
    avg = (Max+Min) // 2
    more = [n for n in arr if n > avg]
    less = [n for n in arr if n < avg]
    if less > more:
      avg += 1
    arr = [(n+avg)//2 for n in arr]
    Max = max(arr)
    Min = min(arr)
    count += 1
    # print(arr)
    if len(ops) <= n:
      ops.append(avg)
  # print(count, ops, n)
  print(count)
  if len(ops) <= n:
    for n in ops: print(n, end=" ")
  if len(ops) <= n:
    print()
