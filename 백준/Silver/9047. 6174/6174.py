import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = input().rstrip()
        cnt = 0
        while True:
            if n == "6174":
                break
            max_n = "".join(sorted(n, reverse=True))
            min_n = max_n[::-1]
            n = str(int(max_n) - int(min_n)).zfill(4)
            cnt += 1
        print(cnt)