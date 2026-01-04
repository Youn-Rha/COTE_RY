import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    S = input().rstrip()
    total = 0
    for s in S:
        total += int(s) ** 5
    print(total)
