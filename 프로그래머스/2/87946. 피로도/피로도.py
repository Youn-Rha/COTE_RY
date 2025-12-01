def solution(k, dungeons):
    answer = [-1]
    d_length = len(dungeons)
    ans = [0] * d_length
    visited = [False] * d_length
    def dfs(t):
        if t == d_length:
            tmp_k = k
            tmp = 0
            for i in range(d_length):
                if tmp_k >= dungeons[ans[i]][0]:
                    tmp += 1
                    tmp_k -= dungeons[ans[i]][1]
                else:
                    break
            answer[0] = max(answer[0], tmp)
        for j in range(d_length):
            if not visited[j]:
                visited[j] = True
                ans[t] = j
                dfs(t + 1)
                visited[j] = False
    dfs(0)
    return answer[0]