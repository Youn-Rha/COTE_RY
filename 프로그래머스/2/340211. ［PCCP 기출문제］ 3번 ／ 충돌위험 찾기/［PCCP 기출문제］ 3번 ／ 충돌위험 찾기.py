from collections import Counter

def solution(points, routes):
    answer = 0
    timeline = []                       # 시간 별 로봇 위치
    for route in routes:
        start_idx = route[0] - 1        # 시작점
        r = points[start_idx][0]
        c = points[start_idx][1]
        time = 0
        timeline.append((r, c, time))
        for i in range(1, len(route)):
            to_idx = route[i] - 1
            to_r = points[to_idx][0]
            to_c = points[to_idx][1]
            while r != to_r:                    # row 먼저 이동
                if r < to_r: r += 1
                else: r -= 1
                time += 1
                timeline.append((r, c, time))   # timeline 기록
            while c != to_c:                    # col 이동
                if c < to_c: c += 1
                else: c -= 1
                time += 1
                timeline.append((r, c, time))   # timeline 기록
                
    timeline = Counter(timeline)
    for t in timeline.values():
        if t > 1:
            answer += 1
    return answer