import sys, collections

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    T = int(input())
    lst = collections.deque((map(int, input().split())))
    students = [0] * 101
    picture1 = []
    picture2 = []
    while len(picture1) != N and len(lst) != 0:
        a = lst.popleft()
        students[a] += 1
        if a not in picture1:
            picture1.append(a)  # 학생 번호
            picture2.append(students[a])  # 학생 인기도
        else:
            picture2[picture1.index(a)] = students[a]

    for l in lst:
        if l in picture1:
            students[l] += 1
            picture2[picture1.index(l)] = students[l]
        else:
            min_std = min(picture2)
            for i in range(N):
                if picture2[i] == min_std:
                    # 삭제
                    picture2.pop(i)
                    students[picture1[i]] = 0   # 삭제되면 인기도 0
                    picture1.pop(i)
                    break

            students[l] += 1
            picture1.append(l)
            picture2.append(students[l])
    print(" ".join(map(str, sorted(picture1))))