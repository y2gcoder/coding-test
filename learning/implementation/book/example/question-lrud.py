"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 110
예제 4-1. 상하좌우
"""
n = int(input())
routes = list(input().split())

# 상하좌우 이동 시 좌표
direction_x = (-1, 1, 0, 0)
direction_y = (0, 0, -1, 1)

x = 1
y = 1

for route in routes:
    current_x = x
    current_y = y
    if route == "U":
        current_x += direction_x[0]
        current_y += direction_y[0]
    elif route == "D":
        current_x += direction_x[1]
        current_y += direction_y[1]
    elif route == "L":
        current_x += direction_x[2]
        current_y += direction_y[2]
    else:
        current_x += direction_x[3]
        current_y += direction_y[3]

    if current_x < 1 or current_y < 1 or current_x > n or current_y > n:
        continue
    else:
        x = current_x
        y = current_y


print(x, y)
