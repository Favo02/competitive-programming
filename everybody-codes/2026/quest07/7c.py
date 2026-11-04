import sys
from collections import defaultdict, deque

graph = defaultdict(list)
lines = sys.stdin.readlines()
orig_energy = defaultdict(int)
LIMIT = 100
LIMIT = 1000000

for line in lines:
    idd, en, connections = line.strip().split(", ")
    idd = idd.split("=")[1]
    en = int(en.split("=")[1])
    connections = connections.split("=")[1].split(",")
    graph[idd] += connections
    orig_energy[idd] = en
    # if len(connections) > len(graph[start]):
    #     start = idd

ans = 0
for start in graph:
    # print("s", start)
    energy = orig_energy.copy()
    banned = set()
    queue = deque()
    amount = {}
    queue.append((start, 10))
    amount[(start, 10)] = 1

    while queue:
        nextamount = {}
        nextqueue = deque()
        while queue:
            (cur, en) = queue.popleft()
            if cur in banned:
                continue
            if en <= 0:
                continue
            amt = amount.pop((cur, en))
            # print(cur, en, "*", amt)
            energy[cur] += en * amt

            for adj in graph[cur]:
                if adj in banned:
                    continue
                if (adj, en - 1) in nextamount:
                    nextamount[(adj, en - 1)] += amt
                else:
                    nextamount[(adj, en - 1)] = amt
                    nextqueue.append((adj, en - 1))

        for idd, en in energy.items():
            if idd in banned:
                continue
            if en >= LIMIT:
                # print("BOOM", idd, en)
                banned.add(idd)
                for adj in graph[idd]:
                    if adj in banned:
                        continue
                    if (adj, 10) in nextamount:
                        nextamount[(adj, 10)] += 1
                    else:
                        nextamount[(adj, 10)] = 1
                        nextqueue.append((adj, 10))

        queue = nextqueue
        amount = nextamount

    # print(sum(e for e in energy.values() if e < LIMIT))
    ans = max(ans, sum(e for e in energy.values() if e < LIMIT))
print(ans)
