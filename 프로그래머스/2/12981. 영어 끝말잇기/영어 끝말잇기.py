def solution(n, words):
    answer = []
    
    words_set = {words[0]}
    
    for i in range(1, len(words)):
        if words[i] not in words_set and words[i][0] == words[i - 1][-1]:
            words_set.add(words[i])
        else:
            return[i % n + 1, i // n + 1]
        

    return [0, 0]