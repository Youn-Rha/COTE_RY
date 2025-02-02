import sys
from heapq import heappop, heappush


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, L = map(int, input().split())
    pq = []
    lst = list(map(int, input().split()))
    for i, l in enumerate(lst):
        heappush(pq, (l, i))  # 값이 key임
        while True:
            value, idx = pq[0]
            if idx <= i - L:  # 유효한 범위 확인
                heappop(pq)
            else:
                break
        print(pq[0][0], end=" ")
