def solution(bandage, health, attacks):
    answer = 0
    a = 0
    h = health
    h_t = 0
    for time in range(1, attacks[-1][0] + 1):
        if h <= 0:
            break
        if time == attacks[a][0]:
            h_t = 0
            h -= attacks[a][1]
            a += 1
        else:
            if h < health:
                h += bandage[1]
                h_t += 1
                if h_t == bandage[0]:
                    h += bandage[2]
                    h_t = 0
                if h >= health:
                    h = health
    if h <= 0:
        answer = -1
    else:
        answer = h
    return answer