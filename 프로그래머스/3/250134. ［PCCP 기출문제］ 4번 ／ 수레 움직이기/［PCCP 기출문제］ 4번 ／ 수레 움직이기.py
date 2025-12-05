from collections import deque

def solution(maze):
    answer = 0
    n = len(maze)
    m = len(maze[0])
    
    r_start, r_end, b_start, b_end = None, None, None, None
    
    for i in range(n):
        for j in range(m):
            tmp = maze[i][j]
            if tmp == 1:
                r_start = (i, j)
            if tmp == 2:
                b_start = (i, j)
            if tmp == 3:
                r_end = (i, j)
            if tmp == 4:
                b_end = (i, j)
    
    queue = deque()
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0 ,0]
    
    queue.append((r_start[0], r_start[1], b_start[0], b_start[1], 0, {r_start}, {b_start}))
    
    # 한번의 이동에 가능한 경로 가지치기
    while queue:
        xr, yr, xb, yb, distance, visited_r, visited_b = queue.popleft()

        # 종료 조건
        if (xr, yr) == r_end and (xb, yb) == b_end:
            return distance
        
        # red/blue 각각 4방향 / 총 16가지 경우 탐색
        rd = [(dx[i], dy[i]) for i in range(4)]
        bd = [(dx[i], dy[i]) for i in range(4)]
        
        # red 또는 blue 가 이미 도착 지점이라면 움직이면 안됨
        if (xr, yr) == r_end:
            rd = [(0, 0)]
        if (xb, yb) == b_end:
            bd = [(0, 0)]
        
        for nnxr, nnyr in rd:
            for nnxb, nnyb in bd:
                nxr = nnxr + xr
                nyr = nnyr + yr
                nxb = nnxb + xb
                nyb = nnyb + yb
            
                # 범위 및 벽 체크
                if not(0 <= nxr < n and 0 <= nyr < m and maze[nxr][nyr] != 5):
                    continue
                if not(0 <= nxb < n and 0 <= nyb < m and maze[nxb][nyb] != 5):
                    continue

                # 서로 같은 자리인 지 체크
                if (nxr, nyr) == (nxb, nyb):
                    continue

                # 서로 크로스로 이동하는 지 체크
                if (nxr, nyr) == (xb, yb) and (nxb, nyb) == (xr, yr):
                    continue

                # 이미 방문 했는 지 체크
                if (nxr, nyr) != r_end and (nxr, nyr) in visited_r: continue
                if (nxb, nyb) != b_end and (nxb, nyb) in visited_b: continue
                
                new_visited_r = visited_r | {(nxr, nyr)}
                new_visited_b = visited_b | {(nxb, nyb)}
                queue.append((nxr, nyr, nxb, nyb, distance + 1, new_visited_r, new_visited_b))

    return answer