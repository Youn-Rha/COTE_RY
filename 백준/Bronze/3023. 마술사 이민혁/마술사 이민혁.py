import sys
from copy import deepcopy

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    R, C = map(int, input().split())
    S = []
    for _ in range(R):
        s = list(input().rstrip())
        S.append(s + s[::-1])
    S.extend(reversed(deepcopy(S)))
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if S[A][B] == "#":
        S[A][B] = "."
    else:
        S[A][B] = "#"
    for a in S:
        print("".join(map(str, a)))