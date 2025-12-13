import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    tmp = list(input().rstrip().split("|"))
    lst = [l[0] for l in tmp]
    C = lst.count("C") + lst.count("F") + lst.count("G")
    A = lst.count("A") + lst.count("D") + lst.count("E")

    if C > A:
        print("C-major")
    elif C < A:
        print("A-minor")
    else:
        S = tmp[-1][-1]
        if S in ["C", "F", "G"]:
            print("C-major")
        else:
            print("A-minor")