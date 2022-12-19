"""
프로그래머스
코딩테스트 연습 - 2019 카카오 개발자 겨울 인턴십
크레인 인형 뽑기
https://school.programmers.co.kr/learn/courses/30/lessons/64061
"""


def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                basket.append(board[j][i - 1])
                board[j][i - 1] = 0
                if len(basket) >= 2:    # 스택처럼 푸는 게 중요함
                    if basket[-2] == basket[-1]:
                        basket.pop()
                        basket.pop()
                        answer += 2
                break

    return answer
