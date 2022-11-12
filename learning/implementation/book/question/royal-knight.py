"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 115
실전 2. 왕실의 나이트
"""
input_data = input()
x = int(input_data[1])
y = ord(input_data[0]) - 96

answer = 0

#
dx = (-1, 1, -1, 1, -2, -2, 2, 2)
dy = (-2, -2, 2, 2, -1, 1, -1, 1)

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        answer += 1


print(answer)
