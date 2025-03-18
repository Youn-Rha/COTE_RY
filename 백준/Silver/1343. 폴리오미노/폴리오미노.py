import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    S = input().rstrip()
    dot = S.replace("X", " ").split()
    X = S.replace(".", " ").split()
    ans = []
    flag = True
    for x in X:
        if len(x) % 2 != 0:
            flag = False
            break
        else:
            A = len(x) // 4
            if len(x) % 4 == 0:
                B = 0
            else:
                B = 1
            ans.append("AAAA" * A + "BB" * B)
    if flag:
        if S[0] == "." and S[-1] == ".":
            print(dot[0], end="")
            for i in range(len(ans)):
                print(ans[i] + dot[i + 1], end="")
        elif S[0] == ".":
            for i in range(len(dot)):
                print(dot[i] + ans[i], end="")
        elif S[-1] == ".":
            for i in range(len(dot)):
                print(ans[i] + dot[i], end="")
        else:
            print(ans[0], end="")
            for i in range(len(dot)):
                print(dot[i] + ans[i + 1], end="")
    else:
        print(-1)