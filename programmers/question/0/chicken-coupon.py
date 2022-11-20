"""
프로그래머스
코딩테스트 연습
치킨 쿠폰
https://school.programmers.co.kr/learn/courses/30/lessons/120884
"""


def solution(chicken):
    answer = 0

    while chicken >= 10:
        answer += chicken // 10
        remain = chicken % 10
        chicken = chicken // 10 + remain

    return answer


def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer


def solution(chicken):
    return int(chicken*0.11111111111)
