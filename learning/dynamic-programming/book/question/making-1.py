"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 217
실전 2. 1로 만들기
"""

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2]) + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3]) + 1
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5]) + 1

print(d[x])

