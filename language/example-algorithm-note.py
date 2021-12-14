# 이것이 코딩 테스트다 with 파이썬, 한빛미디어, 나동빈 저 에서 발췌
''' 2차원 리스트(행렬)를 90도 회전하는 메서드 '''
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res


# 사용 예시
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree(a))
'''
[
    [9, 5, 1],
    [10, 6, 2],
    [11, 7, 3],
    [12, 8, 4],
]
'''