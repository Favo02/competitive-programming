def isValid(arr):
  for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
      return False
  return True

# def solve(arr):




cases = int(input())

while cases > 0:
  cases -= 1
  ig = input()
  arr = input()
  # print(arr)
  arr = [int(n) for n in arr.split(" ")]
  print(arr)

  for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
      solve()
