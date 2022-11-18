"""
프로그래머스
코딩테스트 연습
최댓값 만들기 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120862
"""


def solution(numbers):
    plus_numbers = sorted([i for i in numbers if i >= 0])
    minus_numbers = sorted([i for i in numbers if i < 0])
    if len(plus_numbers) > 1 and len(minus_numbers) > 1:
        return max((plus_numbers[-1] * plus_numbers[-2]), (minus_numbers[0] * minus_numbers[1]))
    elif len(plus_numbers) > 1 and len(minus_numbers) <= 1:
        return plus_numbers[-1] * plus_numbers[-2];
    elif len(plus_numbers) <= 1 and len(minus_numbers) > 1:
        return (minus_numbers[0] * minus_numbers[1])
    else:
        return plus_numbers[0] * minus_numbers[0]


def solution(numbers):
    numbers.sort()
    return max((numbers[0] * numbers[1]), (numbers[-1] * numbers[-2]))
