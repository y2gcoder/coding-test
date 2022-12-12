"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 220
실전 3. 개미 전사
"""

n = int(input())

k = list(map(int, input().split()))

d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])
