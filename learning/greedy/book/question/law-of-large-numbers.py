"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 92
실전 문제 2. 큰 수의 법칙
"""

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
first = numbers[0]
second = numbers[1]

result = 0

while m > k:
    result += (first * k) + (second * 1)
    m -= (k+1)

if m > 0:
    result += first * m

print(result)









