import sys
from collections import deque

inst, sushi = sys.stdin.read().split("\n\n")
inst = inst.strip()

sushi = list(map(lambda s: (int(s.strip().split(",")[0]), int(s.strip().split(",")[1])), sushi.split()))

DIRS = {">": (1, 0), "v": (0, -1), "<": (-1, 0), "^": (0, 1)}

snake = deque()
snake.append((0, 0))
i = 0
for d in inst[:2500]:
    dx, dy = DIRS[d]
    x, y = snake[0][0] + dx, snake[0][1] + dy
    snake.appendleft((x, y))

    if sushi[i] == (x, y):
        i += 1
    else:
        snake.pop()

    if len(set(snake)) != len(snake):
        break

print(len(snake))
