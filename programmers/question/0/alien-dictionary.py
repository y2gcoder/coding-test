"""
프로그래머스
코딩테스트 연습
외계어 사전
https://school.programmers.co.kr/learn/courses/30/lessons/120869
"""


def solution(spell, dic):
    for i in dic:
        count = 0
        for j in spell:
            if j in i:
                count += 1
            if count == len(spell):
                return 1
    return 2


def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):    # set이 비어있을 때, not set() 하면 true
            return 1
    return 2

