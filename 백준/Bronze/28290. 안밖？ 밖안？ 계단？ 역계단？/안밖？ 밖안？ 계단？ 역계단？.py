import sys, math

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline().rstrip()


# main
if __name__ == "__main__":
    S = input()
    if S == "fdsajkl;" or S == "jkl;fdsa":
        print("in-out")
    elif S == "asdf;lkj" or S ==";lkjasdf":
        print("out-in")
    elif S == "asdfjkl;":
        print("stairs")
    elif S == ";lkjfdsa":
        print("reverse")
    else:
        print("molu")