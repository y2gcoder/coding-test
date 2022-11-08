"""
이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈
p. 316
기출 문제 6. 무지의 먹방 라이브
https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3
"""

input_food_times = list(map(int, input().split()))
input_k = int(input())


def solution(food_times, k):
    answer = 0
    index = 0

    for sec in range(1, k + 1):
        if food_times[index % len(food_times)] < 1:
            index += 1

        food_times[index % len(food_times)] -= 1
        index += 1

    if food_times[index % len(food_times)] <= 0:
        answer = -1
    else:
        answer = index % len(food_times) + 1

    return answer



print(solution(input_food_times, input_k))
