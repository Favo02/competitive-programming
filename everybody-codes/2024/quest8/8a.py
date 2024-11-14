blocks = int(input())

used_blocks = 0
width = 1

while used_blocks < blocks:
  used_blocks += width
  width += 2

W = width - 2
KING = used_blocks - blocks
print(W * KING)
