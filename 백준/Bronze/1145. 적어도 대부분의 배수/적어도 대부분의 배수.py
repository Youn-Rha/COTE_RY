import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    lst = list(map(int, input().split()))
    ans = min(lst)
    while True:
        cnt = 0
        for l in lst:
            if ans % l == 0:
                cnt += 1
        if cnt >= 3:
            break
        ans += 1
    print(ans)