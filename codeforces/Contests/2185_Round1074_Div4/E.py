from collections import deque

def solve():
    n, m, k = map(int, input().split())
    robots = list(map(int, input().split()))
    assert len(robots) == n
    spikes = list(map(int, input().split()))
    assert len(spikes) == m
    instr = input()
    assert len(instr) == k

    robots.sort()
    spikes.sort()

    left = []
    right = []

    s = 0
    for r in robots:
        while s+1 < len(spikes) and spikes[s+1] < r:
            s+=1
        if spikes[s] > r:
            left.append(-1)
        else:
            left.append(spikes[s])

    spikes = list(reversed(spikes))
    robots = list(reversed(robots))
    s = 0
    for r in robots:
        while s+1 < len(spikes) and spikes[s+1] > r:
            s+=1
        if spikes[s] < r:
            right.append(-1)
        else:
            right.append(spikes[s])

    spikes = list(reversed(spikes))
    robots = list(reversed(robots))
    right = list(reversed(right))

    toleft = []
    toright = []
    for i in range(len(robots)):

        if left[i] != -1:
            toleft.append((robots[i] - left[i], i))
        if right[i] != -1:
            toright.append((right[i] - robots[i], i))

    toleft.sort()
    toright.sort()
    # print(toleft)
    # print(toright)

    toleft = deque(toleft)
    toright = deque(toright)

    gone = set()
    delta = 0
    for dir in instr:
        if dir == "L":
            delta -= 1
        if dir == "R":
            delta += 1

        while toleft and -delta >= toleft[0][0]:
            gone.add(toleft.popleft()[1])
        while toright and delta >= toright[0][0]:
            gone.add(toright.popleft()[1])

        print(len(robots) - len(gone), end=" ")
    print()

    # print(left, right)
    # print()


cases = int(input())

for _ in range(cases):
    solve()
