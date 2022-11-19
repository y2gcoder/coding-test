"""
프로그래머스
코딩테스트 연습
유한소수 판별하기
https://school.programmers.co.kr/learn/courses/30/lessons/120878
"""

import math


def solution(a, b):
    g = math.gcd(a, b)

    b //= g

    if b == 1:
        return 1

    while b % 2 == 0:
        b //= 2

    while b % 5 == 0:
        b //= 5

    if b == 1:
        return 1

    return 2
