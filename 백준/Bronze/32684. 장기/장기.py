import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    score = [13, 7, 5, 3, 3, 2]

    c, e = 0, 0

    for i in range(6):
        c += lst1[i] * score[i]
        e += lst2[i] * score[i]

    if c > e + 1.5:
        print("cocjr0208")
    else:
        print("ekwoo")