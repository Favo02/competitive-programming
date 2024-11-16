priests = int(input())
div = 1111
blocks = 20240000

# example
# priests = 3
# div = 5
# blocks = 50

def thickness(last):
  return (last * priests) % div

thick = 1
used_blocks = 0
width = 1

while used_blocks < blocks:
  used_blocks += (thick * width)
  width += 2
  thick = thickness(thick)

W = width - 2
KING = used_blocks - blocks
print(W * KING)
