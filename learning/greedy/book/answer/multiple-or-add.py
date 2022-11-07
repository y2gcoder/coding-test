"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 507
기출 문제 2. 곱하기 혹은 더하기
"""

data = input()

# 첫 번째 문자를 숫자로 변형하여 대입
result = int(data[0])
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num


print(result)
