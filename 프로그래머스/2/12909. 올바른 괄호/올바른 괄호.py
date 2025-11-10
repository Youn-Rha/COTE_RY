def solution(S):
    answer = True
    stack = []
    for s in S:
        if s == ')':
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.pop()
        else:
            stack.append(s)
    if len(stack) != 0:
        answer = False

    return answer