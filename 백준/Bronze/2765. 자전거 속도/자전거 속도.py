import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    num = 0
    while True:
        num += 1
        r_inch, spinT, s_time = map(float, input().split())
        if spinT == 0:
            break

        r_feat = r_inch / 12
        r_mile = r_feat / 5280

        m_time = s_time / 60
        h_time = m_time / 60

        l = 3.1415927 * r_mile
        d = spinT * l
        v = d / h_time

        print(f"Trip #{num}: {d:.2f} {v:.2f}")