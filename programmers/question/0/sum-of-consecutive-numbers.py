"""
프로그래머스
코딩테스트 연습
연속된 수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/120923
"""


def solution(num, total):
    value = 1000
    while True:
        sum_value = (num * value) - int((num * (num - 1)) / 2)
        if sum_value == total:
            break
        value -= 1

    return sorted([i for i in range(value, value - num, -1)])


def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]    # 공식 이용해서 풀었네 이사람 굿!
