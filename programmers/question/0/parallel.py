"""
프로그래머스
코딩테스트 연습
평행
https://school.programmers.co.kr/learn/courses/30/lessons/120875
"""


def solution(dots):
    answer = 0
    # 12 34 / 13 24 / 14 23
    first_x = dots[0][0]
    first_y = dots[0][1]
    second_x = dots[1][0]
    second_y = dots[1][1]
    third_x = dots[2][0]
    third_y = dots[2][1]
    fourth_x = dots[3][0]
    fourth_y = dots[3][1]

    if (abs(first_y - second_y) / abs(first_x - second_x)) == (abs(third_y - fourth_y) / abs(third_x - fourth_x)):
        return 1
    if (abs(first_y - third_y) / abs(first_x - third_x)) == (abs(second_y - fourth_y) / abs(second_y - fourth_x)):
        return 1
    if (abs(first_y - fourth_y) / abs(first_x - fourth_x)) == (abs(second_y - third_y) / abs(second_y - third_x)):
        return 1

    return answer


from itertools import combinations

def solution(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))

    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2==x2*y1:
            return 1
    return 0
