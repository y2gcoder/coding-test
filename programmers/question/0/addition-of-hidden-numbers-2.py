"""
프로그래머스
코딩테스트 연습
숨어있는 숫자의 덧셈 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120864
"""


def solution(my_string):
    answer = []

    temp = ""

    for i in my_string:
        if i.isdigit():
            temp += i
        else:
            if len(temp) > 0:
                answer.append(int(temp))
            temp = ""

    if len(temp) > 0:
        answer.append(int(temp))

    return sum(answer)


def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())