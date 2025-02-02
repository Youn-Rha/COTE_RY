import sys
import collections

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, L = map(int, input().split())
    deque = collections.deque()
    lst = list(map(int, input().split()))
    for i, l in enumerate(lst):
        while deque and deque[-1] > l:      # 자신보다 크면 다 지움
            deque.pop()                     # 덱의 맨 앞에는 최솟값이 옴
        deque.append(l)
        if i >= L and deque[0] == lst[i - L]:   # 덱의 맨 앞 원소가
            deque.popleft()                     # 지워야 하면 지움
        print(deque[0], end=" ")
