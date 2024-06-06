import sys


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    S = input().strip()
    dic = dict()
    for s in S:
        dic[s] = dic.get(s, 0) + 1
    cnt = 0
    items = list(dic.items())
    items.sort(key=lambda x: x[0])
    center = ''
    for v in items:
        if v[1] % 2 == 1:
            cnt += 1
            center = v[0]
    result = ""
    if cnt > 1:
        print("I'm Sorry Hansoo")
    else:
        for i in items:
            for _ in range(i[1] // 2):
                result += i[0]
                dic[i[0]] -= 1
        result += center + result[::-1]
        print(result)

