# N x M
n, m = map(int, input().split())
# x, y, 방향
x, y, direction = map(int, input().split())
# 방문한 맵 0으로 생성
visited = [[0] * m for _ in range(n)]
# 첫 위치 정하기
visited[x][y] = 1
# 맵 받기
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))


def turn_left():
    global direction
    if direction == 0:
        direction = 3
    else:
        direction -= 1


result = 1

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def is_sea(target_x, target_y):
    global maps
    return maps[target_x][target_y] == 1

def is_visited(target_x, target_y):
    global visited
    return visited[target_x][target_y] == 1


while True:
    # 왼쪽으로 회전
    turn_left()
    if not is_sea(x+dx[direction], y+dy[direction]) and not is_visited(x+dx[direction], y+dy[direction]):
        x = x + dx[direction]
        y = y + dy[direction]
        visited[x][y] = 1
        result += 1
        continue

    if (is_sea(x+dx[0], y+dy[0]) or is_visited(x+dx[0], y+dy[0])) \
            and (is_sea(x+dx[1], y+dy[1]) or is_visited(x+dx[1], y+dy[1])) \
            and (is_sea(x+dx[2], y+dy[2]) or is_visited(x+dx[2], y+dy[2])) \
            and (is_sea(x+dx[3], y+dy[3]) or is_visited(x+dx[3], y+dy[3])):
        if is_sea(x-dx[direction], y-dy[direction]):
            break
        x = x - dx[direction]
        y = y - dy[direction]
        continue

print(result)

