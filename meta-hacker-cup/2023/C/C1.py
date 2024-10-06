def toBoolArr(buttons):
  arr = []
  for b in buttons:
    if b == '0':
      arr.append(False)
    else:
      arr.append(True)
  return arr

def pressButton(buttons, pressed):
  pressed -= 1
  for i in range(pressed, len(buttons), pressed+1):
    buttons[i] = not buttons[i]
  return buttons

# input = open("small.txt", "r")
# input = open("validation-input.txt", "r")
input = open("full-input.txt", "r")
input = list(map(lambda a: a.split("\n")[0], input))[1:]

cases = []
i = 0
while i < len(input):
  buttons = toBoolArr(input[i+1])
  pressed = []
  j = 0
  while j < int(input[i+2]):
    pressed.append(int(input[i+3+j]))
    j +=1 
  cases.append((buttons, pressed))
  i += 3+j

for i, c in enumerate(cases):
  buttons = c[0]
  pressed = {}
  for p in c[1]:
    if p in pressed:
      pressed[p] += 1
    else:
      pressed[p] = 1
  for k in pressed:
    if pressed[k] % 2 != 0:
      buttons = pressButton(buttons, k)

  res = 0
  for j in range(len(buttons)):
    if buttons[j]:
      buttons = pressButton(buttons, j+1)
      res += 1

  print("Case #", i+1, ": ", res, sep="")
