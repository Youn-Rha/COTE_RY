n, a, b = map(int, input().split())
s, t = map(int, input().split())
s, t = min(s, t), max(s, t)

if a < s and t < b:  # s, t 모두 도시 구간에 있음
    print("City")
elif (t <= a) or (s >= b):  # s, t가 도시 구간을 지나지 않음 = 둘 다 같은 지방 쪽
    print("Outside")
else:
    print("Full")