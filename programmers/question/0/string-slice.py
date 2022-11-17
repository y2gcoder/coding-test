"""
프로그래머스
코딩테스트 연습
잘라서 배열로 저장하기
https://school.programmers.co.kr/learn/courses/30/lessons/120913
"""


def solution(my_str, n):
    answer = []
    l = len(my_str) // n
    if len(my_str) % n > 0:
        l += 1
    for i in range(l):
        answer.append(my_str[i * n: n + i * n])

    return answer


def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]