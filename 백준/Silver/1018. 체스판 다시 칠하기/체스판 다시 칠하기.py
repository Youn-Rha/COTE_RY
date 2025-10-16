import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def check(arr1, arr2):
        cnt = sum(arr1[i][j] != arr2[i][j] for i in range(8) for j in range(8))
        return cnt
    N, M = map(int, input().split())
    lst = [input().rstrip() for _ in range(N)]
    B = ['BWBWBWBW', 'WBWBWBWB'] * 4
    W = ['WBWBWBWB', 'BWBWBWBW'] * 4
    ans = 64
    for i in range(N - 7):
        for j in range(M - 7):
            ans = min(ans, check(B, [row[j:j+8] for row in lst[i:i+8]]))
            ans = min(ans, check(W, [row[j:j+8] for row in lst[i:i+8]]))
    print(ans)