# 2차원 리스트 90도 회전

'''
출처: 이것이 취업을 위한 코딩 테스트다 with 파이썬, 한빛 미디어, 나동빈 P.463
'''

def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result
