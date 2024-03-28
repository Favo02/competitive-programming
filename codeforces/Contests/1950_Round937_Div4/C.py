cases = int(input())

for _ in range(cases):

  string = input()
  # print(string)

  h, m = string.split(":")
  # print(h,m)

  h = int(h)

  ampm = ""

  if int(h) >= 12:
    ampm = "PM"
    h -= 12
  else:
    ampm = "AM"

  if h == 0:
    h = 12

# "{:02d}".format(number)

  print("{:02d}:{} {}".format(h, m , ampm))
