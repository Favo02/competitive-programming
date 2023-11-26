cases = int(input())

while cases > 0:
  cases -= 1
  input()
  arr = [int(n) for n in input().split(" ")]
  # print(arr)

  i = 1
  while i < len(arr)-1:
    # print(i)
    if arr[i-1] < arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
      i = 0
    i += 1
  # print(arr)
  if sorted(arr) == arr:
    print("YES")
  else:
    print("NO")
