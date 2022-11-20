"""
프로그래머스
코딩테스트 연습
A로 B 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/120886
"""


def solution(before, after):
    after_list = list(after)
    for i in before:
        if i in after_list:
            after_list.remove(i)

    return 0 if len(after_list) > 0 else 1


def solution(before, after):
    before = sorted(before)
    after = sorted(after)
    return 1 if before == after else 0
