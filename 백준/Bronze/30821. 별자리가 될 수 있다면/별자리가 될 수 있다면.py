import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def nc5(n):
        return int(math.factorial(n) / (math.factorial(5) * math.factorial(n - 5)))
    N = int(input())
    print(nc5(N))
