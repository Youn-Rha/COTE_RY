import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    A, B, C = map(int, input().split())
    timeline = [0] * 101
    for _ in range(3):
        a, b = map(int, input().split())
        for t in range(a, b):
            timeline[t] += 1
    total = 0
    for count in timeline:
        if count == 1:
            total += (A * 1)
        elif count == 2:
            total += (B * 2)
        elif count == 3:
            total += (C * 3)

    print(total)