"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 359
기출 23. 국영수
"""

n = int(input())

array = []

for i in range(n):
    name, k, e, m = input().split()
    array.append((name, int(k), int(e), int(m)))


result = sorted(array, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in result:
    print(i[0])
