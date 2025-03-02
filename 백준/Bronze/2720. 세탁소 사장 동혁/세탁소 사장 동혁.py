import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    types = [25, 10, 5, 1]
    T = int(input())
    for _ in range(T):
        C = int(input())
        coins = [0, 0, 0, 0]
        for i in range(4):
            coins[i] += C // types[i]
            C %= types[i]
        print(" ".join(map(str, coins)))
