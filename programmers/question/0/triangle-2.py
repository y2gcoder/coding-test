"""
프로그래머스
코딩테스트 연습
삼각형의 완성조건 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120868
"""


def solution(sides):
    answer = 0
    sides.sort()

    # 다른 한 변이 제일 길 때!
    for i in range(sides[1], sum(sides)):
        if i < sum(sides):
            answer += 1

    # sides[1]이 가장 긴 변일 때
    for i in range(sides[1]):
        if i + sides[0] > sides[1]:
            answer += 1

    return answer


def solution(sides):
    # 1. max(sides)가 가장 긴 변일 때 == max(sides) - (max(sides) - min(sides))
    # 2. 다른 한 변이 가장 긴 변일 때 == sum(sides) - max(sides) - 1
    # 1 + 2
    return sum(sides) - max(sides) + min(sides) - 1
