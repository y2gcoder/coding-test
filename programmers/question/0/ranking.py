"""
프로그래머스
코딩테스트 연습
등수 매기기
https://school.programmers.co.kr/learn/courses/30/lessons/120882
"""


def solution(score):
    answer = []
    sorted_array = sorted(score, key=lambda x: sum(x), reverse=True)
    rank_dic = dict()
    ranking = 1
    for i in sorted_array:
        current_sum = sum(i)
        if current_sum not in rank_dic.keys():
            rank_dic[current_sum] = ranking
        ranking += 1

    for i in score:
        answer.append(rank_dic[sum(i)])

    return answer


# 간단하네
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]   # 헉 앞부터 찾으니까 똑같은 등수가 들어가겠구나!!!
