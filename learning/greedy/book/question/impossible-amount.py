"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 314
기출 문제 4. 만들 수 없는 금액
"""

n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0

"""
result 값을 계속 증가시키면서
data로 그 값을 만들 수 있는지 체크...
"""

print(result)
