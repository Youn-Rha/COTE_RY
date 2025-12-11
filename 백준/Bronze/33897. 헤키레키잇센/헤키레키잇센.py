import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    cnt, max_cnt, total_cnt = 1, 0, 1
    for i in range(N - 1):
        if lst[i + 1] < lst[i]:
            total_cnt += 1
            max_cnt = max(max_cnt, cnt)
            cnt = 0
        cnt += 1
    max_cnt = max(max_cnt, cnt)
    print(total_cnt, max_cnt)