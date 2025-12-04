def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start, end = 1, distance
    
    while start <= end:
        mid = (start + end) // 2
        
        prev, remove_cnt = 0, 0
        for rock in rocks:
            if rock - prev < mid:
                remove_cnt += 1
            else:
                prev = rock
        if remove_cnt <= n:
            answer = mid
            start = mid + 1
        else:   
            end = mid - 1
    return answer