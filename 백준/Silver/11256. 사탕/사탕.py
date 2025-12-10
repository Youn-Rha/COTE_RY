import heapq
import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        J, N = map(int, input().split())
        lst = []
        for _ in range(N):
            r, c = map(int, input().split())
            heapq.heappush(lst, - (r * c))
        cnt = 0
        for _ in range(N):
            J += heapq.heappop(lst)
            cnt += 1
            if J <= 0:
                break
        print(cnt)