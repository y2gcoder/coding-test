"""
프로그래머스
코딩테스트 연습
겹치는 선분의 길이
https://school.programmers.co.kr/learn/courses/30/lessons/120876
"""

from itertools import combinations


def solution(lines):
    data = set()
    for (start1, end1), (start2, end2) in combinations(lines, 2):
        if end1 > start2:
            data.update(set([i for i in range(start1, end1 + 1)]) & set([i for i in range(start2, end2 + 1)]))

    if len(data) <= 0:
        return 0

    answer = 0

    array = list(data)
    array.sort()

    for i in range(1, len(array)):
        if array[i] - array[i - 1] == 1:
            answer += 1

    return answer


def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])




