"""
프로그래머스
코딩테스트 연습
배열의 유사도
https://school.programmers.co.kr/learn/courses/30/lessons/120903
"""


def solution(s1, s2):
    answer = 0

    for i in s1:
        for j in s2:
            if i == j:
                answer += 1

    return answer


"""
합집합: |
교집합: &
차집합: -
"""


def solution(s1, s2):
    return len(set(s1) & set(s2))
