def nextNotZero(arr, index):
  for i in range(index, len(arr)):
    if arr[i] > 0:
      return i
  return None

cases = int(input())

while cases > 0:
  cases -= 1
  n = int(input())
  arr = [int(s) for s in input().split(" ")]
  start = max(arr)-1

  res = 0

  up = None
  for i in range(0,len(arr)-1):
    print(i, up, res)

    if up == None:
      if arr[i] < arr[i+1]:
        up = True
      if arr[i] > arr[i+1]:
        up = False
      continue

    if up:
      if arr[i] > arr[i+1]:
        res += 1
        up = False
    else:
      if arr[i] < arr[i+1]:
        res += 1
        up = True
  print(i, up, res)

  print("-->", res-1 + start)
