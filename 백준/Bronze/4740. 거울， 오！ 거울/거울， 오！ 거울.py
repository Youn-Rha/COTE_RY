import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    s = input().rstrip("\n")
    while s != "***":
        print(s[::-1])
        s = input().rstrip("\n")
