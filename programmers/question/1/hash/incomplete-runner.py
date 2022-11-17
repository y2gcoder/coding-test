"""
프로그래머스
코딩테스트 연습
완주하지 못한 선수
https://school.programmers.co.kr/learn/courses/30/lessons/120902
"""


from collections import Counter


def solution(participant, completion):
    map = dict(Counter(participant))
    for i in completion:
        if map[i] > 1:
            map[i] -= 1
        else:
            del map[i]

    for i in map.keys():
        if i in map:
            return i


import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]