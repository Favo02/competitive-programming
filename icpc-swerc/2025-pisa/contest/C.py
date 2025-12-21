t = int(input())
for _ in range(t):
    pan, seq = map(int, input().split())
    pans = []
    hash = {}
    for _ in range(pan):
        panel = list(map(int, input().split()))
        pans.append(panel)
        if pan % 2 == 1:
            hash[tuple(panel[:seq//2])] = panel[seq//2:]

    # print("----------")
    # print(pans)

    if pan % 2 == 0:
        seen = set()
        for panel in pans:
            if panel[0] in seen: continue
            seen.add(panel[0])
            print(*panel, end=" ")
        print()
    else:
        # print("DISPARI")
        # print(hash)
        cur = pans[0][:seq//2]
        print(*cur, end=" ")
        printed = 1
        while printed < pan:
            nextt = hash[tuple(cur)]
            print(*nextt, end=" ")
            cur = nextt
            printed += 1
        print()
