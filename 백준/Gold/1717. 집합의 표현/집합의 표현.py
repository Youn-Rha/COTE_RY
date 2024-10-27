import sys, math

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    # WQU
    def root(i):
        while i != ids[i]:
            i = ids[i]
        return i

    def connected(a, b):
        return root(a) == root(b)

    def union(p, q):
        a, b = root(p), root(q)
        if a == b:
            return
        if size[a] <= size[b]:
            ids[a] = b
            size[b] += size[a]
        else:
            ids[b] = a
            size[a] += size[b]




    n, m = map(int, input().split())
    ids = [i for i in range(n + 1)]
    size = [1 for _ in range(n + 1)]
    for i in range(m):
        o, a, b = map(int, input().split())
        if o:
            if connected(a, b):
                print("YES")
            else:
                print("NO")
        else:
            union(a, b)