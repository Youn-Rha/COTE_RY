def solution(expressions):
    def convert(num, n):
        s = ''
        while num:
            s += str(num % n)
            num //= n
        s += str(num)
        return int(s[::-1])
        
    answer = []
    answer_tmp = []
    min_num = 0
    for expression in expressions:
        for e in expression:
            if e.isdigit():
                min_num = max(min_num, int(e))
    # 진법 후보 리스트
    lst = list(range(min_num + 1, 10))
    
    for expression in expressions:
        a, op, b, _, c = expression.split()
        # 구해야되는 표현식은 따로 빼두기
        if c == 'X':
            answer_tmp.append(expression)
            continue
        tmp = []
        for l in lst:
            aa = int(a, l)
            bb = int(b, l)
            cc = int(c, l)
            if op == '+':
                if aa + bb == cc:
                    tmp.append(l)
            else:
                if aa - bb == cc:
                    tmp.append(l)
        # 진법 후보 리스트 업데이트
        lst = tmp
    # X 찾기
    for ans in answer_tmp:
        lst_set = set()
        a, op, b, _, c = ans.split()
        for l in lst:
            aa = int(a, l)
            bb = int(b, l)
            if op == '+':
                c = convert(aa + bb, l)
            else:
                c = convert(aa - bb, l)
            lst_set.add(c)
        if len(lst_set) != 1:   # 진법이 여러개인 경우
            c = '?'

        answer.append(ans.replace('X', str(c)))
    
    return answer