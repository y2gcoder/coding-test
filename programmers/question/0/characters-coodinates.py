"""
프로그래머스
코딩테스트 연습
캐릭터의 좌표
https://school.programmers.co.kr/learn/courses/30/lessons/120861
"""


def solution(keyinput, board):
    start_x = -((board[0] - 1) // 2)
    start_y = -((board[1] - 1) // 2)
    end_x = ((board[0] - 1) // 2)
    end_y = ((board[1] - 1) // 2)

    answer = [0, 0]

    dir = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}

    for i in keyinput:
        nx = answer[0] + dir[i][0]
        ny = answer[1] + dir[i][1]

        if nx >= start_x and nx <= end_x and ny >= start_y and ny <= end_y:
            answer[0] = nx
            answer[1] = ny

    return answer

