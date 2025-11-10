def solution(want, number, discount):
    answer = 0
    want_num = []
    for i in range(len(want)):
        for _ in range(number[i]):
            want_num.append(want[i])
    print(want_num)
    for i in range(len(discount) - len(want_num) + 1):
        if sorted(want_num) == sorted(discount[i:i + len(want_num)]):
            answer += 1
    return answer