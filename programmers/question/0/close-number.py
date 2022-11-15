"""
프로그래머스
코딩테스트 연습
가까운 수
https://school.programmers.co.kr/learn/courses/30/lessons/120890
"""


def solution(array, n):
    min_index = 0

    for i in range(len(array)):
        if abs(array[i] - n) < abs(array[min_index] - n):
            min_index = i
        elif abs(array[i] - n) == abs(array[min_index] - n):
            if array[i] < array[min_index]:
                min_index = i

    return array[min_index]


def solution(array, n):
    array.sort(key = lambda v: (abs(v -n), v-n))
    return array[0]