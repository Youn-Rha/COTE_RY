import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    s1 = input().rstrip()
    s2 = input().rstrip()
    dp = [[0] * 1001 for _ in range(1001)]
    # 한글자씩 추가하면서 비교하기
    for i in range(len(s1)):
        for j in range(len(s2)):
            # 비교하는 글자가 같으면 그 이전의 문자열끼리의 LCS + 1
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            # 다르면 그 이전의 LCS의 최대값
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    print(dp[len(s1)][len(s2)])