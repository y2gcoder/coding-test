"""
프로그래머스
코딩테스트 연습
약수의 개수와 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/77884
"""


def solution(left, right):
    plus = []
    minus = []

    for i in range(left, right + 1):
        data = []
        for j in range(1, i + 1):
            if i % j == 0:
                data.append(j)

        if len(data) % 2 == 0:
            plus.append(i)
        else:
            minus.append(i)

    return sum(plus) - sum(minus)


"""
제곱수의 약수는 홀수개 인 것을 이용한 방법
"""


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i

    return answer
