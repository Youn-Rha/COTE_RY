import sys

#sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    A, B = map(int, input().split())
    cnt = 0
    while B != A:
        if B % 10 == 1 and B > A:
            B -= 1
            B = int(str(B)[:-1])
        elif B < A or B % 2 == 1:
            cnt = -2
            break
        else:
            B //= 2
        cnt += 1
    print(cnt + 1)