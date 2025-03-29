import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, W = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        U, V = map(int, input().split())
        tree[U].append(V)
        tree[V].append(U)
    cnt = 0
    for i in range(2, N + 1):
        if len(tree[i]) == 1:
            cnt += 1
    print(W / cnt)
