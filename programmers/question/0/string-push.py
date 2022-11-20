"""
프로그래머스
코딩테스트 연습
문자열 밀기
https://school.programmers.co.kr/learn/courses/30/lessons/120921
"""


def solution(A, B):
    answer = 0
    if A == B:
        return 0
    for _ in range(len(A)):
        answer += 1
        A = A[-1] + A[:-1]
        if A == B:
            break

    if answer >= len(A):
        return -1

    return answer


solution=lambda a,b:(b*2).find(a)
