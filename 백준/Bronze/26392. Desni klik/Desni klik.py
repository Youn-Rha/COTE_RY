t, n, m = map(int, input().split())
for _ in range(t):
    graph = [list(input()) for _ in range(n)]
    up = 0
    down = n-1
    while up < n and not graph[up].count('#'):
        up += 1
    while down >= 0 and not graph[down].count('#'):
        down -= 1
    print(down-up)