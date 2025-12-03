def solution(bandage, health, attacks):
    last_attack = attacks[-1][0]    # 마지막 공격 시간
    healing = 0                     # 연속 회복 횟수
    cur_health = health             # 현재 체력
    
    # 빠른 공격 시간 조회를 위해 {시간 : 공격력} 값으로 딕셔너리에 저장
    attacks = {key : value for key, value in attacks}

    for i in range(last_attack + 1):
        if i in attacks:            # 공격 시간 조회
            cur_health -= attacks[i]# 공격 받음
            healing = 0             # 연속 회복 횟수 초기화
            if cur_health <= 0:
                return -1
        else:
            cur_health = min(health, cur_health + bandage[1]) # 최대 체력 유지
            healing += 1
            if healing == bandage[0]:   # 연속 회복했을 때 추가 체력
                cur_health = min(health, cur_health + bandage[2]) # 최대 체력 유지
                healing = 0             # 연속 회복 횟수 초기화
                
    return cur_health