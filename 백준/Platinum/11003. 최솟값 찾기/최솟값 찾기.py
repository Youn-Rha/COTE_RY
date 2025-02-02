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
        while deque and deque[-1] > l:
            deque.pop()
        deque.append(l)
        if i >= L and deque[0] == lst[i - L]:
            deque.popleft()
        print(deque[0], end=" ")
