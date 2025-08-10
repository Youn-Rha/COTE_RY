import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    vowel = "aeiou"
    S = input().rstrip()
    cnt = 0
    for s in S:
        if s in vowel:
            cnt += 1
    print(cnt, cnt + S.count('y'))