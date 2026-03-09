import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def check():
        bingo = 0
        for i in range(5):
            if sum(board[i]) == 5:
                bingo += 1
        for j in range(5):
            tmp = 0
            for i in range(5):
                tmp += board[i][j]
            if tmp == 5:
                bingo += 1
        tmp = 0
        for i in range(5):
            tmp += board[i][i]
        if tmp == 5:
            bingo += 1
        tmp = 0
        for i in range(5):
            tmp += board[i][4 - i]
        if tmp == 5:
            bingo += 1

        if bingo >= 3:
            return True
        return False

    board = [[0 for _ in range(5)] for _ in range(5)]
    bingo = {}
    for i in range(5):
        tmp = list(map(int, input().split()))
        for j in range(5):
            bingo[tmp[j]] = (i, j)
    ans = []
    for _ in range(5):
        ans.extend(list(map(int, input().split())))

    for i, num in enumerate(ans):
        x, y = bingo[num]
        board[x][y] = 1
        if check():
            print(i + 1)
            break