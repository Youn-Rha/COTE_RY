import sys, heapq


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    V, E = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(V + 1)]
    distance = [float('INF')] * (V + 1)
    distance[start] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    queue = [[0, start]]

    while queue:
        w, v = heapq.heappop(queue)
        if distance[v] < w:
            continue
        for e in graph[v]:
            if w + e[1] < distance[e[0]]:
                distance[e[0]] = w + e[1]
                heapq.heappush(queue, [w + e[1], e[0]])

    for i in range(1, V + 1):
        if distance[i] == float('INF'):
            print("INF")
        else:
            print(distance[i])
