"""
프로그래머스
코딩테스트 연습
종이 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/120922
"""


def solution(M, N):
    return (min(M, N) - 1) + (min(M, N) * (max(M, N) - 1))


def solution(M, N):
    return M * N - 1
