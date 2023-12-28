cases = int(input())

for _ in range(cases):
  line = None
  for _ in range(3):
    inn = input()
    if '?' in inn:
      line = inn
  if 'A' not in line:
    print('A')
  elif 'B' not in line:
    print('B')
  elif 'C' not in line:
    print('C')
