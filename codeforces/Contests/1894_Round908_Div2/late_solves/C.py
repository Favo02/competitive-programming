def solve(arr, k):
  if k == -1:
    return True

  for i,c in enumerate(arr):
    if c > len(arr): continue

    shiftedI = (i + c) % len(arr)
    if shiftedI != c-1: continue

    if solve(rshift(list.copy(arr), c), k-1):
      return True

  return False

def rshift(arr, n):
  return arr[-n:] + arr[:-n]

inputs = int(input())
while inputs > 0:
  inputs -= 1
  _, k = input().split(" ")
  k = int(k)
  arr = input().split(" ")
  arr = [int(n) for n in arr]

  if len(arr) == 1:
    # print("innn", arr)
    if arr[0] == 1:
      print("Yes")
    else:
      print("No")
    continue

  # print(arr, k)
  if solve(arr, k):
    print("Yes")
  else:
    print("No")

