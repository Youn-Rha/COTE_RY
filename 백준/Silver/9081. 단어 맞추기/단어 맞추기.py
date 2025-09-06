import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s = list(input().rstrip())
        for i in range(len(s) - 1, 0, -1):
            if s[i] > s[i - 1]:
                for j in range(len(s) - 1, 0, -1):
                    if s[i - 1] < s[j]:
                        s[i - 1], s[j] = s[j], s[i - 1]
                        break
                s = s[:i] + s[i:][::-1]
                break
        print("".join(s))