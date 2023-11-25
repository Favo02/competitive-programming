cases = int(input())

while cases > 0:
  cases -= 1
  input()
  str = input()
  # print(str)

  count = 0
  lastB = str.rfind("B")
  firstA = str.find("A")
  if lastB == -1 or firstA == -1:
    print(0)
  else:
    print(max(0,lastB-firstA))




  # aFound = False
  # for i,s in enumerate(str[:-1]):
    # print(i,s)
    # if s == 'A': aFound = True
    # if not aFound: continue
    # if i < lastB:
      # print("yes")
      # count += 1
    # else: break
  # print(count)
