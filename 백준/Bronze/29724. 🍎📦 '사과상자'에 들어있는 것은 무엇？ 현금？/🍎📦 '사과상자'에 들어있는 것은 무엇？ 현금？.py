import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    A_w, B_w, A_p = 0, 0, 0
    for _ in range(N):
        T, W, H, L = input().split()
        if T == 'A':
            A = (int(W) // 12) * (int(H) // 12) * (int(L) // 12)
            A_w += 1000 + A * 500
            A_p += A * 4000
        else:
            B_w += 6000
    print(A_w + B_w)
    print(A_p)
