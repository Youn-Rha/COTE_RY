import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    origin = "SciComLove"
    S = input().rstrip()
    cnt = 0
    for i in range(len(S)):
        if S[i] != origin[i]:
            cnt += 1
    print(cnt)