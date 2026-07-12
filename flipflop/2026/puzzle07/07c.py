import sys
from collections import deque

inst, sushi = sys.stdin.read().split("\n\n")
inst = inst.strip()

sushi = list(map(lambda s: (int(s.strip().split(",")[0]), int(s.strip().split(",")[1])), sushi.split()))

DIRS = {">": (1, 0), "v": (0, -1), "<": (-1, 0), "^": (0, 1)}

snake = deque()
snake.append((0, 0))
eats = 0
s = 0
for d in inst:
    dx, dy = DIRS[d]
    x, y = snake[0][0] + dx, snake[0][1] + dy
    snake.appendleft((x, y))

    if sushi[s] == (x, y):
        s += 1
    else:
        snake.pop()

    for i, (sx, sy) in enumerate(list(snake)):
        if i == 0:
            continue
        if (x, y) == (sx, sy):
            snake = deque(list(snake)[:i-1])
            eats += 1

    assert len(set(snake)) == len(snake)

print(len(snake) * eats)
