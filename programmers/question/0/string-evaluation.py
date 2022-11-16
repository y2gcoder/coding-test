"""
프로그래머스
코딩테스트 연습
문자열 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/120902
"""


def solution(my_string):
    return eval(my_string)


def solution(my_string):
    return sum(int(i) for i in my_string.replace(" - ", " + -").split(" + "))

