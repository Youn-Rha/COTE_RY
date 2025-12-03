def solution(video_len, pos, op_start, op_end, commands):
    for command in commands:
        # 시작하는 pos 대비용
        if op_start <= pos <= op_end:
            pos = op_end
        mm, ss = int(pos[:2]), int(pos[3:])
        if command == "prev":
            ss -= 10
            if ss < 0:          # 초가 -로 넘어갈 때
                if mm == 0:
                    ss = 0
                else:
                    mm -= 1     # 60 빌려줌
                    ss += 60    # 분에서 60을 빌려옴 
            pos = f"{mm:02d}:{ss:02d}"
        elif command == "next":
            ss += 10
            if ss >= 60:        # 초가 60 이상일 때 분으로 1 올라감
                mm += 1
                ss -= 60
            # 10초 뒤로 갔을 때 비디오 전체 길이보다 큰 경우
            if mm >= int(video_len[:2]) and ss >= int(video_len[3:]):
                mm, ss = int(video_len[:2]), int(video_len[3:])
            pos = f"{mm:02d}:{ss:02d}"
    # next 이후의 상황 대비용
    if op_start <= pos <= op_end:
            pos = op_end
    return pos