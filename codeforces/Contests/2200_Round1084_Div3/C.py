from collections import deque

def solve():
    n = int(input())
    s = input()
    assert len(s) == n

    stack = deque()
    for ss in s:
        if stack and stack[-1] == ss:
            stack.pop()
        else:
            stack.append(ss)
    return not stack

for _ in range(int(input())):
    print("YES" if solve() else "NO")
