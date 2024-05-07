import sys

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    dial = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
            5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
            8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}

    words = input()
    total = 0
    for word in words:
        for key in dial.keys():
            if word in dial[key]:
                total += key + 1
    print(total)
