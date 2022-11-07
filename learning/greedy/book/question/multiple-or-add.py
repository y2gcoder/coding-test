"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 312
기출 문제 2. 곱하기 혹은 더하기
"""

data = input()

result = 0
for i in data:
    number = int(i)
    if result <= 1 or number <= 1:
        result += number
    else:
        result *= number

print(result)
