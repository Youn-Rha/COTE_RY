import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    return


if __name__ == "__main__":
    N, M = map(int, input().split())
    words = {}
    for i in range(N):
        word = input().rstrip()
        if len(word) >= M:
            # dict 안에 있으면 값 / 없으면 0 반환
            words[word] = words.get(word, 0) + 1          
            
    # 다중으로 sort 조건 줄 때 (-) 붙이면 reverse 의미
    words = sorted(list(words.items()), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for word in words:
        print(word[0])
