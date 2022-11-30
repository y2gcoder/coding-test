"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 178
실전 2. 위에서 아래로
"""

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')
