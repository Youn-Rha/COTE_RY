import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    R, C = map(int, input().split())
    Rg, Cg, Rp, Cp = map(int, input().split())
    lst = ""
    for _ in range(R):
        lst += input().rstrip()
    if lst.count("P") != Rp * Cp:
        print(1)
    else:
        print(0)