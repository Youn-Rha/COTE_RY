import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def check():
        if board[0][0] != -1 and (board[0][0] == board[0][1] == board[0][2]):
            print(N)
            exit(0)
        elif board[1][0] != -1 and (board[1][0] == board[1][1] == board[1][2]):
            print(N)
            exit(0)
        elif board[2][0] != -1 and (board[2][0] == board[2][1] == board[2][2]):
            print(N)
            exit(0)
        elif board[0][0] != -1 and (board[0][0] == board[1][0] == board[2][0]):
            print(N)
            exit(0)
        elif board[0][1] != -1 and (board[0][1] == board[1][1] == board[2][1]):
            print(N)
            exit(0)
        elif board[0][2] != -1 and (board[0][2] == board[1][2] == board[2][2]):
            print(N)
            exit(0)
        elif board[0][0] != -1 and (board[0][0] == board[1][1] == board[2][2]):
            print(N)
            exit(0)
        elif board[2][0] != -1 and (board[2][0] == board[1][1] == board[0][2]):
            print(N)
            exit(0)
    N = int(input())
    board = [[-1] * 3 for _ in range(3)]
    for _ in range(9):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        board[x][y] = N
        check()
        N ^= 0b11
    print(0)