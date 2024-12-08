import sys


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    cinema = [['.' for _ in range(20)] for _ in range(10)]
    N = int(input())
    for _ in range(N):
        s = input().rstrip()
        row = ord(s[0]) - ord('A')
        col = int(s[1:]) - 1
        cinema[row][col] = 'o'
    for c in cinema:
        print("".join(map(str, c)))