"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 118
실전 3. 게임 개발
"""

n, m = map(int, input().split())
a, b, d = map(int, input().split())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
cd = 0
cx = a
cy = b

data[a][b] = 2


# 반시계 방향으로 전환
def rotate(current_dir):
    if current_dir == 0:
        return 3
    else:
        return current_dir - 1


# 네 방향 모두 막혀있는지 확인
def movable(x, y):
    for j in range(4):
        if data[x + dx[j]][y + dy[j]] == 0:
            return True
    return False


while True:
    cd = rotate(cd)
    mx = cx + dx[cd]
    my = cy + dy[cd]
    if data[mx][my] == 0:
        cx = mx
        cy = my
        data[cx][cy] = 2
        count += 1
        continue
    if not movable(cx, cy):
        mx = cx - dx[cd]
        my = cy - dy[cd]
        if data[mx][my] == 1:
            break
        else:
            cx = mx
            cy = my
            continue


print(count)
