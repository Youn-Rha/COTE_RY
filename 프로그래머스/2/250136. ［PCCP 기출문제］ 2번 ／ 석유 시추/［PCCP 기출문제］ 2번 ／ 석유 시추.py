from collections import deque

def solution(land):
    def bfs(x, y):
        total = 1
        col_set = set()
        da = [0, 0, -1, 1]
        db = [1, -1, 0, 0]
        queue = deque()
        queue.append((x, y))
        col_set.add(y)
        while queue:
            a, b = queue.popleft()
            for i in range(4):
                na = a + da[i]
                nb = b + db[i]
                if na < 0 or na >= n or nb < 0 or nb >= m:
                    continue
                if not visited[na][nb] and land[na][nb] == 1:
                    visited[na][nb] = True
                    queue.append((na, nb))
                    col_set.add(nb)
                    total += 1
        return total, col_set
    
    n = len(land)
    m = len(land[0])
    answer = [0] * m
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                visited[i][j] = True
                oil, oil_set = bfs(i, j)
                for o in oil_set:
                    answer[o] += oil
                
    return max(answer)