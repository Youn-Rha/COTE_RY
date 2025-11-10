import math

def solution(progresses, speeds):
    answer = []
    launch = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    start = launch[0]
    cnt = 1
    for i in range(1, len(launch)):
        if start < launch[i]:
            start = launch[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
            
    return answer