"""
프로그래머스
코딩테스트 연습
안전지대
https://school.programmers.co.kr/learn/courses/30/lessons/120866
"""


def solution(board):
    n = len(board[0])

    mines = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                mines.append((i, j))

    for i in mines:
        start_x = i[0] - 1 if (i[0] - 1) >= 0 else i[0]
        start_y = i[1] - 1 if (i[1] - 1) >= 0 else i[1]
        end_x = i[0] + 1 if i[0] + 1 < n else i[0]
        end_y = i[1] + 1 if i[1] + 1 < n else i[1]

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if board[x][y] == 0:
                    board[x][y] = 2

    return sum([i.count(0) for i in board])


def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
