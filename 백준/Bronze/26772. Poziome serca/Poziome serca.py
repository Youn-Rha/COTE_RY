import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    print(" @@@   @@@  " * N)
    print("@   @ @   @ " * N)
    print("@    @    @ " * N)
    print("@         @ " * N)
    print(" @       @  " * N)
    print("  @     @   " * N)
    print("   @   @    " * N)
    print("    @ @     " * N)
    print("     @      " * N)