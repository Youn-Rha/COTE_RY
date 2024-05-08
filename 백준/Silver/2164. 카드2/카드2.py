import sys
from collections import deque

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    cards = [i for i in range(1, N + 1)]
    cards = deque(cards)
    while len(cards) != 1:
        cards.popleft()
        a = cards.popleft()
        cards.append(a)

    print(cards[0])
