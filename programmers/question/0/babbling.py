"""
프로그래머스
코딩테스트 연습
옹알이 (1)
https://school.programmers.co.kr/learn/courses/30/lessons/120956
"""


def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for j in possible:
            babbling[i] = babbling[i].replace(j, ' ')

    answer = list(map(lambda x: x.strip(), babbling))
    return answer.count('')


def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for j in possible:
            b = b.replace(j, ' ')
        if len(b.strip()) == 0:
            answer += 1

    return answer
