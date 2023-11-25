cases = int(input())

while cases > 0:
  cases -= 1
  line1 = input().split(" ")
  n, x = int(line1[0]), int(line1[1])

  # print(n,x)

  line2 = input()
  stations = [int(s) for s in line2.split(" ")]
  # print(stations)

  maxD = max(stations[0], (x-stations[-1])*2)
  for i in range(len(stations)-1):
    d = stations[i+1] - stations[i]
    maxD = max(maxD, d)

  print(maxD)
