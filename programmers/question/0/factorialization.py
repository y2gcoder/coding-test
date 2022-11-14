"""
프로그래머스
코딩테스트 연습
소인수분해
https://school.programmers.co.kr/learn/courses/30/lessons/120852
"""


# def solution(n):
#     answer = []
#
#     target = 2
#
#     while n > 1:
#         while n % target == 0:
#             n = n // target
#             answer.append(target)
#         target += 1
#     answer = list(set(answer))
#     answer.sort()
#
#     return answer


def solution(n):
    answer = []

    target = 2

    while target <= n:
        if n % target == 0:
            n //= target
            if target not in answer:
                answer.append(target)
        else:
            target += 1

    return answer
