"""
프로그래머스
코딩테스트 연습
합성수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120846
"""


def solution(n):
    array = []

    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:  # 자기 자신 말고도 나누어떨어지면 합성수!
                array.append(i)

    return len(set(array))