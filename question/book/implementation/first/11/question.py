from collections import deque

n = int(input())

# 보드 만들자
board = [[0] * n for _ in range(n)]

k = int(input())

# 사과 넣자
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 3 # 사과는 3

l = int(input())
# 북, 동, 남, 서 방향 정리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn = []
for _ in range(l):
    x, c = input().split()
    turn.append((int(x), c))

direction = 1


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 오른쪽으로 회전
def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0


second = 0  # 게임 시간
# 뱀 머리
headX = 0
headY = 0
snake = deque([(headX, headY)])   # 뱀 초기화
board[headX][headY] = 1 #뱀 시작 초기화
while True:
    second += 1
    headX += dx[direction]
    headY += dy[direction]

    if headX < 0 or headX >= n or headY < 0 or headY >= n:    # 벽에 부딪혔을 때
        break

    if board[headX][headY] == 1:    # 자기 자신과 부딪혔을 때
        break

    if board[headX][headY] == 0:    # 아무것도 없을 때
        board[headX][headY] = 1
        snake.appendleft((headX, headY))
        tail = snake.pop()
        board[tail[0]][tail[1]] = 0

    if board[headX][headY] == 3:    # 사과!
        board[headX][headY] = 1
        snake.appendleft((headX, headY))

    for t in turn:
        if t[0] == second:
            if t[1] == 'L':
                turn_left()
            if t[1] == 'D':
                turn_right()

print(second)
