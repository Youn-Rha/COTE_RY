import sys


def input():
    return sys.stdin.readline()


def recur(depth):
    global cnt
    if depth == len(s) and cnt < int(n):
        cnt += 1
        if cnt == int(n):
            res.append(ans.copy())
            return
        return
    for i in range(len(s)):
        if not visited[i]:
            visited[i] = True
            ans[depth] = s[i]
            recur(depth + 1)
            visited[i] = False


# main
if __name__ == "__main__":
    while True:
        try:
            s, n = input().split()
            ans = [""] * len(s)
            visited = [False] * len(s)
            res = []
            cnt = 0
            recur(0)
            if len(res) == 0:
                print(s, n, "= No permutation")
            else:
                print(s, n, "=", "".join(res[0]))
        except:
            break
