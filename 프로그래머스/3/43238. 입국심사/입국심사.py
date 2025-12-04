def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    
    while start <= end:
        t = (start + end) // 2
        possible_n = 0
        for time in times:
            possible_n += t // time
        if possible_n >= n:
            answer = t
            end = t - 1
        else:
            start = t + 1
    return answer