"""
프로그래머스
코딩테스트 연습
저주의 숫자 3
https://school.programmers.co.kr/learn/courses/30/lessons/120871
"""


def solution(n):
    answer = []

    current_value = 0
    while True:
        current_value += 1
        if current_value % 3 != 0 and '3' not in str(current_value):
            answer.append(current_value)

        if len(answer) >= n:
            break

    return answer[-1]


def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
