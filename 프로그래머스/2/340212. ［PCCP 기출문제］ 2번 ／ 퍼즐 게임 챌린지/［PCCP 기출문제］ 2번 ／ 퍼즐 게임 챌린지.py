def solution(diffs, times, limit):
    answer = 0
    start = 1
    end = max(diffs)
    # 시간 축약을 위한 이분 탐색 시작
    while start <= end:
        level = (start + end) // 2
        cur_time = 0
        # 전체 소요 시간 계산
        for i in range(len(diffs)):
            if diffs[i] <= level:
                cur_time += times[i]
            else:
                cur_time += (diffs[i] - level) * (times[i - 1] + times[i]) + times[i]
        # 소요 시간이 limit 보다 작으면 level 낮춰서 다시 계산
        if cur_time <= limit:
            answer = level
            end = level - 1
        # 반대 경우 level 올려서 다시 계산
        else:
            start = level + 1
    
    return answer