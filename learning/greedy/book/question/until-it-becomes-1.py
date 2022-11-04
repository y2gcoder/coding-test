"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 99
실전 문제 4. 1이 될 때까지
"""
n, k = map(int, input().split())

count = 0
while True:
    if n == 1:
        break
    elif n % k == 0:
        n /= k
        count += 1
    else:
        n = n - 1
        count += 1

print(count)
