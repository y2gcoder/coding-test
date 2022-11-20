"""
프로그래머스
코딩테스트 연습
이진수 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/120885
"""


def solution(bin1, bin2):
    return format(int(bin1, 2) + int(bin2, 2), 'b')


def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer
