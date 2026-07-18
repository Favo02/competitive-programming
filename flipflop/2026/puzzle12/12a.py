import sys

numbers, cards = sys.stdin.read().split("\n\n")
numbers = list(map(int, (" ".join(map(str.strip, numbers.splitlines()))).split()))
cards = [list(map(int, card.split())) for card in cards.splitlines()]

rows = [[0] * 5 for _ in range(len(cards))]
cols = [[0] * 5 for _ in range(len(cards))]
diagl = [0] * len(cards)
diagr = [0] * len(cards)

assert len(numbers) == len(set(numbers))

bingo = 0

for num in numbers:
    for ic, c in enumerate(cards):
        for i, n in enumerate(c):
            if num == n:
                assert rows[ic][i // 5] < 5
                rows[ic][i // 5] += 1
                if rows[ic][i // 5] == 5:
                    bingo += 1

                assert cols[ic][i % 5] < 5
                cols[ic][i % 5] += 1
                if cols[ic][i % 5] == 5:
                    bingo += 1

                if i in {0, 6, 12, 18, 24}:
                    assert diagl[ic] < 5
                    diagl[ic] += 1
                    if diagl[ic] == 5:
                        bingo += 1

                if i in {4, 8, 12, 16, 20}:
                    assert diagr[ic] < 5
                    diagr[ic] += 1
                    if diagr[ic] == 5:
                        bingo += 1

    if bingo >= 5:
        print(num)
        break
