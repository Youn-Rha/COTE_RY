import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    row_list = [True] * 10
    col_list = [True] * 10
    for i in range(10):
        tmp = list(input().rstrip())
        for j in range(10):
            if tmp[j] == 'o':
                row_list[i] = False
                col_list[j] = False
    ans = 20
    for i in range(10):
        for j in range(10):
            if row_list[i] and col_list[j]:
                ans = min(ans, abs(i - r) + abs(j - c))
    print(ans)