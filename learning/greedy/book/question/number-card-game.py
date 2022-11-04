"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 97
실전 문제 3. 숫자 카드 게임
"""
n, m = map(int, input().split())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

min_numbers = []

for i in range(n):
    min_numbers.append(min(data[i]))

print(max(min_numbers))
