import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    S = input().rstrip()
    S = S.replace("pi", "00")
    S = S.replace("ka", "00")
    S = S.replace("chu", "000")
    if S == "0" * len(S):
        print("YES")
    else:
        print("NO")