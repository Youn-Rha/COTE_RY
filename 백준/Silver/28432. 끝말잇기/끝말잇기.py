import heapq
import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    start, end = '', ''
    lst = []
    for _ in range(N):
        lst.append(input().rstrip())
    M = int(input())
    ans = []
    for _ in range(M):
        ans.append(input().rstrip())
    if N == 1:
        print(ans[0])
        exit(0)
    for i in range(N):
        if lst[i] == "?":
            for s in ans:
                if i == 0:
                    end = lst[i + 1][0]
                    if s[-1] == end and s not in lst:
                        print(s)
                        break
                elif i == N - 1:
                    start = lst[i - 1][-1]
                    if s[0] == start and s not in lst:
                        print(s)
                        break
                else:
                    start, end = lst[i - 1][-1], lst[i + 1][0]
                    if s[0] == start and s[-1] == end and s not in lst:
                        print(s)
                        break
            break
