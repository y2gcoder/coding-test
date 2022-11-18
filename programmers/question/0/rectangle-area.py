"""
프로그래머스
코딩테스트 연습
직사각형 넓이 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120860
"""


def solution(dots):
    dx = set()
    dy = set()

    for i in dots:
        dx.add(i[0])
        dy.add(i[1])
    list_dx = list(dx)
    list_dy = list(dy)
    x = abs(list_dx[0] - list_dx[1])
    y = abs(list_dy[0] - list_dy[1])

    return x * y


def solution(dots):
    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])
