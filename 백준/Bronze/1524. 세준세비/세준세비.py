import heapq
import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input()
        N, M = map(int, input().split())
        S = list(map(int, input().split()))
        B = list(map(int, input().split()))
        heapq.heapify(S)
        heapq.heapify(B)
        while not(len(S) == 0 or len(B) == 0):
            if S[0] >= B[0]:
                heapq.heappop(B)
            else:
                heapq.heappop(S)
        print("S" if len(S) > len(B) else "B")