"""
프로그래머스
코딩테스트 연습
다음에 올 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/120924
"""


def solution(common):
    if common[1] == (common[0] + common[2]) / 2:  # 등차중항
        return common[-1] + (common[1] - common[0])
    elif common[1] ** 2 == common[0] * common[2]:  # 등비중항
        return common[-1] * int(common[1] / common[0])


def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer
