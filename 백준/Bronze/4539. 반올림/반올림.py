import sys
import decimal


context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        n = input()
        tmp, digit = 10, -1
        while int(n) > tmp:
            n = round(decimal.Decimal(n), digit)
            tmp *= 10
            digit -= 1
        print(int(n))
