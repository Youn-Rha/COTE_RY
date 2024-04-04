import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    return


if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    lst_set = set(lst)
    lst_set = sorted(list(lst_set))
    lst_dic = dict()
    ans = []
    # 인덱스가 자신의 앞에 있는 원소의 개수임
    for i in range(len(lst_set)):
        lst_dic[lst_set[i]] = i
    # 딕셔너리 접근은 O(1)의 시간복잡도를 가짐
    for l in lst:
        ans.append(lst_dic[l])
    print(" ".join(map(str, ans)))