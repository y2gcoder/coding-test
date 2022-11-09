"""
프로그래머스
코딩테스트 연습
탐욕법
https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""

input_n = int(input())
input_lost = list(map(int, input().split()))
input_reserve = list(map(int, input().split()))


def solution(n, lost, reserve):
    answer = 0
    data = [1] * (n + 1)
    data[0] = -1
    for r in reserve:
        data[r] += 1
    for l in lost:
        data[l] -= 1

    for i in range(1, n + 1):
        if data[i] < 2:
            continue
        if i == 1:
            if data[i + 1] < 1:
                data[i] -= 1
                data[i + 1] += 1
        elif i == n:
            if data[i - 1] < 1:
                data[i] -= 1
                data[i - 1] += 1
        else:
            if data[i - 1] < 1:
                data[i] -= 1
                data[i - 1] += 1
            elif data[i + 1] < 1:
                data[i] -= 1
                data[i + 1] += 1
            else:
                continue

    answer = data.count(1)
    answer += data.count(2)

    return answer


print(solution(input_n, input_lost, input_reserve))
