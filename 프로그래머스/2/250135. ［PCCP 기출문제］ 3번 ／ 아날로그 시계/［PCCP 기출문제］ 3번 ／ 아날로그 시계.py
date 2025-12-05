def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    # 12시간 = 720분 = 43200초
    # 1초 당 돌아가는 각도 -> 초침 - 6도 / 분침 - 0.1도 / 시침 - 1/120도
    start = h1 * 60 * 60 + m1 * 60 + s1
    end = h2 * 60 * 60 + m2 * 60 + s2
    
    # 처음 시작할 때 겹치는 경우
    if (h1 == 0 and m1 == 0 and s1 == 0) or (h1 == 12 and m1 == 0 and s1 == 0):
        answer += 1
    
    for i in range(start, end):
        cur_s = (i * 6) % 360
        cur_m = (i / 10) % 360
        cur_h = (i / 120) % 360
        
        next_s = ((i + 1) * 6) % 360
        next_m = ((i + 1) / 10) % 360
        next_h = ((i + 1) / 120) % 360
        
        if next_s == 0: next_s = 360
        if next_m == 0: next_m = 360
        if next_h == 0: next_h = 360
        
        # 초침 - 시침 비교
        if cur_s < cur_h and next_s >= next_h:
            answer += 1
        
        # 초침 - 분침 비교
        if cur_s < cur_m and next_s >= next_m:
            answer += 1
            
        # 분침/시침 동시 비교 (중복 제거용)
        if next_s == next_m == next_h:
            answer -= 1
    
    return answer