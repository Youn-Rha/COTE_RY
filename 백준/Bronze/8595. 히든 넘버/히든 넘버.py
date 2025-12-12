import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    n = int(input())
    S = input().rstrip()
    ans = 0
    tmp = "0"
    for s in S:
        if s.isdecimal():
           tmp += s
        else:
            ans += int(tmp)
            tmp = "0"
    ans += int(tmp)
    print(ans)