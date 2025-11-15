from collections import deque
from math import ceil

# def pace(station):
#     res = []
#     cur = 5
#     for _ in range(ceil(abs(station) / 2)+1):
#         res.append(paces[cur])
#         nextcur = (cur + 1) if station > 0 else (cur - 1)
#         cur = max(0, min(len(paces)-1, nextcur))

#     if station % 2 == 1:
#         res += (res[:-1])[::-1]
#     else:
#         res += res[::-1]

#     return " ".join(map(str, res))


n = int(input())

def MOVEMENT(pace):
    if pace == 0:
        return 0
    if pace < 0:
        return -1
    if pace > 0:
        return +1

def CHANGEPACE(ipace, move):
    return max(0, min(len(P)-1, ipace+move))


P = [-1, -2, -3, -4, -5, 0, 5, 4, 3, 2, 1]

for _ in range(n):
    station, timelimit = input().split()
    timelimit = int(timelimit)
    sx, sy = map(int, station.split(","))
    # ax, ay = map(int, input().split(","))

    def bfs():
        q = deque()
        q.append((0, 0, 0, 0, 0, 0, 0)) # time, x, y, ipacex, ipacey, remx, remy
        seen = set()
        while q:
            time, x, y, ipacex, ipacey, remx, remy = q.popleft()
            print(f"x{x=}, y{y=}, {ipacex=}, {ipacey=}, {remx=}, {remy=}")
            if time > timelimit:
                continue
            # if (x, y, ipacex, ipacey, remx, remy) in seen:
            #     continue
            # seen.add((x, y, ipacex, ipacey, remx, remy))

            if sx == x and sy == y:
                return time

            if remx == 0 and remy == 0:
                q.append((time+1,
                        x + MOVEMENT(P[ipacex]), y + MOVEMENT(P[ipacey]),
                        CHANGEPACE(ipacex, +1), CHANGEPACE(ipacey, +1),
                        abs(P[CHANGEPACE(ipacex, +1)]), abs(P[CHANGEPACE(ipacey, +1)])))
                q.append((time+1,
                        x + MOVEMENT(P[ipacex]), y + MOVEMENT(P[ipacey]),
                        CHANGEPACE(ipacex, -1), CHANGEPACE(ipacey, +1),
                        abs(P[CHANGEPACE(ipacex, -1)]), abs(P[CHANGEPACE(ipacey, +1)])))
                q.append((time+1,
                        x + MOVEMENT(P[ipacex]), y + MOVEMENT(P[ipacey]),
                        CHANGEPACE(ipacex, +1), CHANGEPACE(ipacey, -1),
                        abs(P[CHANGEPACE(ipacex, +1)]), abs(P[CHANGEPACE(ipacey, -1)])))
                q.append((time+1,
                        x + MOVEMENT(P[ipacex]), y + MOVEMENT(P[ipacey]),
                        CHANGEPACE(ipacex, -1), CHANGEPACE(ipacey, -1),
                        abs(P[CHANGEPACE(ipacex, -1)]), abs(P[CHANGEPACE(ipacey, -1)])))
                continue
            if remx == 0:
                assert remy > 0
                q.append((time+1,
                        x + MOVEMENT(P[ipacex]), y,
                        CHANGEPACE(ipacex, +1), ipacey,
                        abs(P[CHANGEPACE(ipacex, +1)]), remy-1))
                q.append((time+1,
                        x + MOVEMENT(P[ipacex]), y,
                        CHANGEPACE(ipacex, -1), ipacey,
                        abs(P[CHANGEPACE(ipacex, -1)]), remy-1))
                continue
            if remy == 0:
                assert remx > 0
                q.append((time+1,
                        x, y + MOVEMENT(P[ipacey]),
                        ipacex, CHANGEPACE(ipacey, +1),
                        remx-1, abs(P[CHANGEPACE(ipacey, +1)])))
                q.append((time+1,
                        x, y + MOVEMENT(P[ipacey]),
                        ipacex, CHANGEPACE(ipacey, -1),
                        remx-1, abs(P[CHANGEPACE(ipacey, -1)])))
                continue
            assert remy > 0
            assert remx > 0
            q.append((time+1, x, y, ipacex, ipacey, remx-1, remy-1))

    print(bfs())

