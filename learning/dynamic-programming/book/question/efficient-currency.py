"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 226
실전 5. 효율적인 화폐구성
"""
n, m = map(int, input().split())

array = []


for _ in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] != 10001:
    print(-1)
else:
    print(d[m])
